package me.xingz.file;

import me.xingz.schema.Schema;
import me.xingz.schema.SchemaField;

import java.io.*;

public class Deaggregator {
    private final Schema schema;
    private final String filenamePrefix = "/Users/xzhou/Developer/xing/stockfiles/";

    public Deaggregator(Schema schema) {
        this.schema = schema;
    }

    public void deaggregate(String filename, long timestamp) throws IOException {
        File file = new File(filename);
        FileReader fileReader = new FileReader(file);
        BufferedReader br = new BufferedReader(fileReader);
        String line;

        while ((line = br.readLine()) != null) {
            String[] parts = line.split(",(?=([^\"]*\"[^\"]*\")*[^\"]*$)");
//            System.out.println(line);
//            System.out.println(parts.length + "\t" + parts);
            if (parts.length != schema.getSchemaFields().size()) throw new IllegalArgumentException();

            String outputFilename = "error";
            StringBuilder sb = new StringBuilder();
            sb.append(timestamp + ",");
            for (int i = 0; i < parts.length; i++) {
                String processedStr = handlePart(parts[i], schema.get(i));
                if (i == 0) {
                    outputFilename = processedStr;
                    continue;
                }
                sb.append(processedStr);
                if (i != parts.length - 1) sb.append(",");
            }
            sb.append("\n");
            writeToFile(filenamePrefix + outputFilename + ".csv", sb.toString());
        }
    }

    public void writeToFile(String filename, String line) {
        BufferedWriter bw = null;
        FileWriter fw = null;

        try {
            File file = new File(filename);

            // if file doesnt exists, then create it
            if (!file.exists()) {
                file.createNewFile();
            }
            // true = append file
            fw = new FileWriter(file.getAbsoluteFile(), true);
            bw = new BufferedWriter(fw);
            bw.write(line);
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            try {
                if (bw != null)
                    bw.close();
                if (fw != null)
                    fw.close();
            } catch (IOException ex) {
                ex.printStackTrace();
            }
        }
    }

    public String handlePart(String part, SchemaField schemaField) {
        switch (schemaField.getType()) {
            case bool:
                break;
            case string:
                return part.substring(1, part.length() - 1);
            case decimal:
                return String.valueOf(Double.valueOf(part));
            case integer:
                break;
            case percent:
                part = part.replaceAll("%", "").replaceAll("\"", "");
                double d = Double.valueOf(part) / 100;
                d = Math.round(d * 10000.0) / 10000.0;
                return String.valueOf(d);
            case timestamp:
                break;
            default:
                throw new IllegalArgumentException();
        }
        return part;
    }

    public static void main(String[] args) throws IOException {
//        Schema schema = new Schema()
//                .withSchemaField(SchemaField.string())  // ID
////                .withSchemaField(SchemaField.string())  // Name
//                .withSchemaField(SchemaField.decimal()) // ask
//                .withSchemaField(SchemaField.decimal()) // bid
//                .withSchemaField(SchemaField.decimal()) // change
//                .withSchemaField(SchemaField.percent()) // percent change
//                .withSchemaField(SchemaField.decimal()) // 52 week low
//                .withSchemaField(SchemaField.decimal()) // 52 week high
//                .withSchemaField(SchemaField.percent()) // 52 week low percent
//                .withSchemaField(SchemaField.percent()) // 52 week high percent
//                .withSchemaField(SchemaField.decimal()) // target
//                ;
//        Deaggregator d = new Deaggregator(schema, "/Users/xzhou/Developer/xing/test.csv", System.currentTimeMillis());
//        d.deaggregate();
    }
}

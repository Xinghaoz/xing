package me.xingz;
import me.xingz.schema.Schema;
import me.xingz.schema.SchemaField;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class Conf {

    @Bean
    public Schema schema() {
        Schema schema = new Schema()
                .withSchemaField(SchemaField.string())  // ID
//                .withSchemaField(SchemaField.string())  // Name
                .withSchemaField(SchemaField.decimal()) // ask
                .withSchemaField(SchemaField.decimal()) // bid
                .withSchemaField(SchemaField.decimal()) // change
                .withSchemaField(SchemaField.percent()) // percent change
                .withSchemaField(SchemaField.decimal()) // 52 week low
                .withSchemaField(SchemaField.decimal()) // 52 week high
                .withSchemaField(SchemaField.percent()) // 52 week low percent
                .withSchemaField(SchemaField.percent()) // 52 week high percent
                .withSchemaField(SchemaField.decimal()) // target
                ;

        return schema;
    }
}

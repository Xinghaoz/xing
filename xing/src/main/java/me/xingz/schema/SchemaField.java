package me.xingz.schema;

import java.util.Enumeration;
import java.util.Properties;
import java.util.ResourceBundle;

public class SchemaField {
    private boolean required;
    private Type type;

    public enum Type {
        string,
        integer,
        decimal,
        percent,
        bool,
        timestamp
    }

    public SchemaField(Type type, boolean required) {
        this.type = type;
        this.required = required;
    }

    public static SchemaField integer() {
        return new SchemaField(Type.integer, false);
    }

    public static SchemaField string() {
        return new SchemaField(Type.string, false);
    }

    public static SchemaField timestamp() {
        return new SchemaField(Type.timestamp, false);
    }

    public static SchemaField decimal() {
        return new SchemaField(Type.decimal, false);
    }

    public static SchemaField percent() {
        return new SchemaField(Type.percent, false);
    }

    public static SchemaField bool() {
        return new SchemaField(Type.bool, false);
    }

    public SchemaField require() {
        this.required = true;
        return this;
    }

    public boolean isRequired() {
        return required;
    }

    public Type getType() {
        return type;
    }

    public static void main(String[] args) {
        String className = SchemaField.class.getSimpleName();
        String rootKey = className + ".";
        Properties properties = new Properties();

        ResourceBundle bundle = ResourceBundle.getBundle("lambda");
        Enumeration<String> keya = bundle.getKeys();
        while(keya.hasMoreElements()) {
            String key = keya.nextElement();
            System.out.println("key = " + key);
            properties.setProperty(key, bundle.getString(key));
        }

        Properties classProperties = new Properties();
        for (String name : properties.stringPropertyNames()) {
            if (name.startsWith(rootKey)) {
                classProperties.setProperty(name.substring(rootKey.length(), name.length()), (String) properties.get(name));
            }
        }

//        return new ClassProperties(className, classProperties);
    }
}

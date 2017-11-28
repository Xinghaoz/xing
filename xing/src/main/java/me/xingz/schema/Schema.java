package me.xingz.schema;

import java.util.ArrayList;
import java.util.List;

public class Schema {
    List<SchemaField> schemaFields = new ArrayList<>();

    public Schema withSchemaField(SchemaField sf) {
        this.schemaFields.add(sf);
        return this;
    }

    public SchemaField get(int i) {
        return schemaFields.get(i);
    }

    public List<SchemaField> getSchemaFields() {
        return schemaFields;
    }
}

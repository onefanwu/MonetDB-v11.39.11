unsigned char _40_json_sql[2783] = {
"create schema json;\n"
"create type json external name json;\n"
"create function json.filter(js json, pathexpr string)\n"
"returns json external name json.filter;\n"
"GRANT EXECUTE ON FUNCTION json.filter(json, string) TO PUBLIC;\n"
"create function json.filter(js json, name tinyint)\n"
"returns json external name json.filter;\n"
"GRANT EXECUTE ON FUNCTION json.filter(json, tinyint) TO PUBLIC;\n"
"create function json.filter(js json, name integer)\n"
"returns json external name json.filter;\n"
"GRANT EXECUTE ON FUNCTION json.filter(json, integer) TO PUBLIC;\n"
"create function json.filter(js json, name bigint)\n"
"returns json external name json.filter;\n"
"GRANT EXECUTE ON FUNCTION json.filter(json, bigint) TO PUBLIC;\n"
"create function json.text(js json, e string)\n"
"returns string external name json.text;\n"
"GRANT EXECUTE ON FUNCTION json.text(json, string) TO PUBLIC;\n"
"create function json.number(js json)\n"
"returns float external name json.number;\n"
"GRANT EXECUTE ON FUNCTION json.number(json) TO PUBLIC;\n"
"create function json.\"integer\"(js json)\n"
"returns bigint external name json.\"integer\";\n"
"GRANT EXECUTE ON FUNCTION json.\"integer\"(json) TO PUBLIC;\n"
"create function json.isvalid(js string)\n"
"returns bool external name json.isvalid;\n"
"GRANT EXECUTE ON FUNCTION json.isvalid(string) TO PUBLIC;\n"
"create function json.isobject(js string)\n"
"returns bool external name json.isobject;\n"
"GRANT EXECUTE ON FUNCTION json.isobject(string) TO PUBLIC;\n"
"create function json.isarray(js string)\n"
"returns bool external name json.isarray;\n"
"GRANT EXECUTE ON FUNCTION json.isarray(string) TO PUBLIC;\n"
"create function json.isvalid(js json)\n"
"returns bool external name json.isvalid;\n"
"GRANT EXECUTE ON FUNCTION json.isvalid(json) TO PUBLIC;\n"
"create function json.isobject(js json)\n"
"returns bool external name json.isobject;\n"
"GRANT EXECUTE ON FUNCTION json.isobject(json) TO PUBLIC;\n"
"create function json.isarray(js json)\n"
"returns bool external name json.isarray;\n"
"GRANT EXECUTE ON FUNCTION json.isarray(json) TO PUBLIC;\n"
"create function json.length(js json)\n"
"returns integer external name json.length;\n"
"GRANT EXECUTE ON FUNCTION json.length(json) TO PUBLIC;\n"
"create function json.keyarray(js json)\n"
"returns json external name json.keyarray;\n"
"GRANT EXECUTE ON FUNCTION json.keyarray(json) TO PUBLIC;\n"
"create function json.valuearray(js json)\n"
"returns json external name json.valuearray;\n"
"GRANT EXECUTE ON FUNCTION json.valuearray(json) TO PUBLIC;\n"
"create function json.text(js json)\n"
"returns string external name json.text;\n"
"GRANT EXECUTE ON FUNCTION json.text(json) TO PUBLIC;\n"
"create aggregate json.tojsonarray( x string ) returns string external name aggr.jsonaggr;\n"
"GRANT EXECUTE ON AGGREGATE json.tojsonarray( string ) TO PUBLIC;\n"
"create aggregate json.tojsonarray( x double ) returns string external name aggr.jsonaggr;\n"
"GRANT EXECUTE ON AGGREGATE json.tojsonarray( double ) TO PUBLIC;\n"
};
#include "monetdb_config.h"
#include "sql_import.h"
#ifdef _MSC_VER
#undef read
#pragma section(".CRT$XCU",read)
#endif
LIB_STARTUP_FUNC(init_40_json_sql)
{ sql_register("40_json", _40_json_sql); }

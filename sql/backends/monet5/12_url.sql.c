unsigned char _12_url_sql[2171] = {
"CREATE TYPE url EXTERNAL NAME url;\n"
"CREATE function getAnchor( theUrl url ) RETURNS STRING\n"
"EXTERNAL NAME url.\"getAnchor\";\n"
"GRANT EXECUTE ON FUNCTION getAnchor(url) TO PUBLIC;\n"
"CREATE function getBasename(theUrl url) RETURNS STRING\n"
"EXTERNAL NAME url.\"getBasename\";\n"
"GRANT EXECUTE ON FUNCTION getBasename(url) TO PUBLIC;\n"
"CREATE function getContext(theUrl url) RETURNS STRING\n"
"EXTERNAL NAME url.\"getContext\";\n"
"GRANT EXECUTE ON FUNCTION getContext(url) TO PUBLIC;\n"
"CREATE function getDomain(theUrl url) RETURNS STRING\n"
"EXTERNAL NAME url.\"getDomain\";\n"
"GRANT EXECUTE ON FUNCTION getDomain(url) TO PUBLIC;\n"
"CREATE function getExtension(theUrl url) RETURNS STRING\n"
"EXTERNAL NAME url.\"getExtension\";\n"
"GRANT EXECUTE ON FUNCTION getExtension(url) TO PUBLIC;\n"
"CREATE function getFile(theUrl url) RETURNS STRING\n"
"EXTERNAL NAME url.\"getFile\";\n"
"GRANT EXECUTE ON FUNCTION getFile(url) TO PUBLIC;\n"
"CREATE function getHost(theUrl url) RETURNS STRING\n"
"EXTERNAL NAME url.\"getHost\";\n"
"GRANT EXECUTE ON FUNCTION getHost(url) TO PUBLIC;\n"
"CREATE function getPort(theUrl url) RETURNS STRING\n"
"EXTERNAL NAME url.\"getPort\";\n"
"GRANT EXECUTE ON FUNCTION getPort(url) TO PUBLIC;\n"
"CREATE function getProtocol(theUrl url) RETURNS STRING\n"
"EXTERNAL NAME url.\"getProtocol\";\n"
"GRANT EXECUTE ON FUNCTION getProtocol(url) TO PUBLIC;\n"
"CREATE function getQuery(theUrl url) RETURNS STRING\n"
"EXTERNAL NAME url.\"getQuery\";\n"
"GRANT EXECUTE ON FUNCTION getQuery(url) TO PUBLIC;\n"
"CREATE function getUser(theUrl url) RETURNS STRING\n"
"EXTERNAL NAME url.\"getUser\";\n"
"GRANT EXECUTE ON FUNCTION getUser(url) TO PUBLIC;\n"
"CREATE function getRobotURL(theUrl url) RETURNS STRING\n"
"EXTERNAL NAME url.\"getRobotURL\";\n"
"GRANT EXECUTE ON FUNCTION getRobotURL(url) TO PUBLIC;\n"
"CREATE function isaURL(theUrl string) RETURNS BOOL\n"
"EXTERNAL NAME url.\"isaURL\";\n"
"GRANT EXECUTE ON FUNCTION isaURL(string) TO PUBLIC;\n"
"CREATE function newurl(protocol STRING, hostname STRING, \"port\" INT, file STRING)\n"
"RETURNS url\n"
"EXTERNAL NAME url.\"new\";\n"
"GRANT EXECUTE ON FUNCTION newurl(STRING, STRING, INT, STRING) TO PUBLIC;\n"
"CREATE function newurl(protocol STRING, hostname STRING, file STRING)\n"
"RETURNS url\n"
"EXTERNAL NAME url.\"new\";\n"
"GRANT EXECUTE ON FUNCTION newurl(STRING, STRING, STRING) TO PUBLIC;\n"
};
#include "monetdb_config.h"
#include "sql_import.h"
#ifdef _MSC_VER
#undef read
#pragma section(".CRT$XCU",read)
#endif
LIB_STARTUP_FUNC(init_12_url_sql)
{ sql_register("12_url", _12_url_sql); }

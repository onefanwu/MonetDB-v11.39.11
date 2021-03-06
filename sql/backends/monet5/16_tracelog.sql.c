unsigned char _16_tracelog_sql[164] = {
"create function sys.tracelog()\n"
"returns table (\n"
"ticks bigint,\n"
"stmt string\n"
")\n"
"external name sql.dump_trace;\n"
"create view sys.tracelog as select * from sys.tracelog();\n"
};
#include "monetdb_config.h"
#include "sql_import.h"
#ifdef _MSC_VER
#undef read
#pragma section(".CRT$XCU",read)
#endif
LIB_STARTUP_FUNC(init_16_tracelog_sql)
{ sql_register("16_tracelog", _16_tracelog_sql); }

package com.jd.jim.testframework.executor.enums;

/**
 * Description:
 * Author: wangjinshuai
 * Date: 2020-12-15 20:23
 * Email: wangjinshuai@jd.com
 */
public enum CommandEnum {

    SET("SET", "set", "setHandler"),
    SETNX("SETNX", "setnx", "setNXHandler"),
    SETEX("SETEX", "setex", "setEXHandler"),
    GET("GET", "get", "getHandler"),
    GETSET("GETSET", "getset", "getsetHandler"),
    APPEND("APPEND", "append", "appendHandler"),
    STRLEN("STRLEN", "strlen", "strlenHandler"),
    SETRANGE("SETRANGE", "setrange", "setRangeHandler"),
    GETRANGE("GETRANGE", "getrange", "getRangeHandler"),
    PSETEX("PSETEX", "psetex", "psetexHandler"),
    MSET("MSET", "mset", "mSetHandler"),
    MSETNX("MSETNX", "msetnx", "msetnxHandler"),
    MGET("MGET", "mget", "mgetHandler"),
    DECR("DECR", "decr", "decrHandler"),
    DECRBY("DECRBY", "decrby", "decrbyHandler"),
    INCR("INCR", "incr", "incrHandler"),
    INCRBY("INCRBY", "incrby", "incrbyHandler"),
    INCRBYFLOAT("INCRBYFLOAT", "incrbyfloat", "incrByFloatHandler"),


    LPUSH("LPUSH", "lpush", "lpushHandler"),
    LPOP("LPOP", "lpop", "lpopHandler"),
    LPUSHX("LPUSHX", "lpushx", "lpushxHandler"),
    RPUSH("RPUSH", "rpush", "rpushHandler"),
    RPUSHX("RPUSHX", "rpushx", "rpushxHandler"),
    RPOP("RPOP", "rpop", "rpopHandler"),
    RPOPLPUSH("RPOPLPUSH", "rpoplpush", "rpoplpushHandler"),
    LREM("LREM", "lrem", "lremHandler"),
    LLEN("LLEN", "llen", "llenHandler"),
    LINDEX("LINDEX", "lindex", "lindexHandler"),
    LINSERT("LINSERT", "linsert", "linsertHandler"),
    LSET("LSET", "lset", "lsetHandler"),
    LRANGE("LRANGE", "lrange", "lrangeHandler"),
    LTRIM("LTRIM", "ltrim", "ltrimHandler"),

    HSET("HSET", "hset", "hSetHandler"),
    HSETNX("HSETNX", "hsetnx", "hSetNXHandler"),
    HGET("HGET", "hget", "hGetHandler"),
    HEXISTS("HEXISTS", "hexists", "hExistsHandler"),
    HDEL("HDEL", "hdel", "hDelHandler"),
    HLEN("HLEN", "hlen", "hLenHandler"),
    HSTRLEN("HSTRLEN", "hstrlen", "hStrLenHandler"),
    HINCRBY("HINCRBY", "hincrby", "hIncrByHandler"),
    HINCRBYFLOAT("HINCRBYFLOAT", "hincrbyfloat", "hIncrByFloatHandler"),
    HMSET("HMSET", "hmset", "hMSetHandler"),
    HMGET("HMGET", "hmget", "hMGetHandler"),
    HKEYS("HKEYS", "hkeys", "hKeysHandler"),
    HVALS("HVALS", "hvals", "hValsHandler"),
    HGETALL("HGETALL", "hgetall", "hGetAllHandler"),
    HSCAN("HSCAN", "hscan", "hScanHandler"),

    SADD("SADD", "sadd", "saddHandler"),
    SISMEMBER("SISMEMBER", "sismember", "sismemberHandler"),
    SPOP("SPOP", "spop", "spopHandler"),
    SRANDMEMBER("SRANDMEMBER", "srandmember", "srandmemberHandler"),
    SREM("SREM", "srem", "sremHandler"),
    SMOVE("SMOVE", "smove", "smoveHandler"),
    SCARD("SCARD", "scard", "scardHandler"),
    SMEMBERS("SMEMBERS", "smembers", "smembersHandler"),
    SSCAN("SSCAN", "sscan", "sscanHandler"),
    SINTER("SINTER", "sinter", "sinterHandler"),
    SINTERSTORE("SINTERSTORE", "sinterstore", "sinterstoreHandler"),
    SUNION("SUNION", "sunion", "sunionHandler"),
    SUNIONSTORE("SUNIONSTORE", "sunionstore", "sunionstoreHandler"),
    SDIFF("SDIFF", "sdiff", "sdiffHandler"),
    SDIFFSTORE("SDIFFSTORE", "sdiffstore", "sdiffstoreHandler"),

    ZADD("ZADD", "zadd", "zAddHandler"),
    ZSCORE("ZSCORE", "zscore", "zScoreHandler"),
    ZINCRBY("ZINCRBY", "zincrby", "zIncrByHandler"),
    ZCARD("ZCARD", "zcard", "zCardHandler"),
    ZCOUNT("ZCOUNT", "zcount", "zCountHandler"),
    ZRANGE("ZRANGE", "zrange", "zRangeHandler"),
    ZREVRANGE("ZREVRANGE", "zrevrange", "zRevRangeHandler"),
    ZRANGEBYSCORE("ZRANGEBYSCORE", "zrangebyscore", "zRangeByScoreHandler"),
    ZREVRANGEBYSCORE("ZREVRANGEBYSCORE", "zrevrangebyscore", "zRevRangeByScoreHandler"),
    ZRANK("ZRANK", "zrank", "zRankHandler"),
    ZREVRANK("ZREVRANK", "zrevrank", "zRevRankHandler"),
    ZREM("ZREM", "zrem", "zRemHandler"),
    ZREMRANGEBYRANK("ZREMRANGEBYRANK", "zremrangebyrank", "zRemRangeByRankHandler"),
    ZREMRANGEBYSCORE("ZREMRANGEBYSCORE", "zremrangebyscore", "zRemRangeByScoreHandler"),
    ZRANGEBYLEX("ZRANGEBYLEX", "zrangebylex", "zRangeByLexHandler"),
    ZLEXCOUNT("ZLEXCOUNT", "zlexcount", "zLexCountHandler"),
    ZREMRANGEBYLEX("ZREMRANGEBYLEX", "zremrangebylex", "zRemRangeByLexHandler"),
    ZSCAN("ZSCAN", "ZSCAN", "zScanHandler"),
    ZUNIONSTORE("ZUNIONSTORE", "zunionstore", "zUnionStoreHandler"),
    ZINTERSTORE("ZINTERSTORE", "zinterstore", "zInterStoreHandler"),

    EVAL("EVAL", "eval", "evalHandler"),
    EVALSHA("EVALSHA", "evalsha", "evalshaHandler"),

    AUTH("AUTH", "auth", "authHandler"),

    PING("PING", "ping", "pingHandler"),
    ECHO("ECHO", "echo", "echoHandler"),
    OBJECT("OBJECT", "object", "objectHandler"),

    DUMP("DUMP", "dump", "dumpHandler"),
    RESTORE("RESTORE", "restore", "restoreHandler"),

    PFADD("PFADD", "pfadd", "pfAddHandler"),
    PFCOUNT("PFCOUNT", "pfcount", "pfCountHandler"),
    PFMERGE("PFMERGE", "pfmerge", "pfMergeHandler"),

    SETBIT("SETBIT", "setbit", "setBitHandler"),
    GETBIT("GETBIT", "getbit", "getBitHandler"),
    BITCOUNT("BITCOUNT", "bitcount", "bitCountHandler"),
    BITPOS("BITPOS", "bitpos", "bitPosHandler"),
    BITOPO("BITOP", "bitop", "bitOpHandler"),
    BIFIELD("BIFIELD", "bifield", "bitFieldHandler"),

    EXISTS("EXISTS", "exists", "existsHandler"),
    TYPE("TYPE", "type", "typeHandler"),
    RENAME("RENAME", "rename", "renameHandler"),
    RENAMENX("RENAMENX", "renamenx", "renameNXHandler"),
    MOVE("MOVE", "move", "moveHandler"),
    DEL("DEL", "del", "delHandler"),
    RANDOMKEY("RANDOMKEY", "randomkey", "randomKeyHandler"),
    DBSIZE("DBSIZE", "dbsize", "dbSizeHandler"),
    KEYS("KEYS", "keys", "keysHandler"),
    SCAN("SCAN", "scan", "scanHandler"),
    SORT("SORT", "sort", "sortHandler"),
    FLUSHDB("FLUSHDB", "flushdb", "flushDBHandler"),
    FLUSHALL("FLUSHALL", "flushall", "flushAllHandler"),
    SELECT("SELECT", "select", "selectHandler"),
    SWAPDB("SWAPDB", "swapdb", "swapDBHandler"),
    MULTI("MULTI", "multi", "multiHandler"),

    EXPIRE("EXPIRE", "expire", "expireHandler"),
    EXPIREAT("EXPIREAT", "expireat", "expireAtHandler"),
    TTL("TTL", "ttl", "ttlHandler"),
    PERSIST("PERSIST", "persist", "persistHandler"),
    PEXPIRE("PEXPIRE", "pexpire", "pExpireHandler"),
    PEXPIREAT("PEXPIREAT", "pexpireat", "pExpireAtHandler"),
    PTTL("PTTL", "pttl", "pTtlHandler"),

    UNKNOWN("UNKNOWN", "unknown", ""),
    ;

    CommandEnum(String type, String name, String handlerClassName) {
        this.type = type;
        this.name = name;
        this.handlerClassName = handlerClassName;
    }

    /**
     * 获取命令枚举
     * @param type
     * @return
     */
    public static CommandEnum getCommandEnumByType(String type) {
        for (CommandEnum commandEnum : CommandEnum.values()) {
            if (commandEnum.getType().equalsIgnoreCase(type)) {
                return commandEnum;
            }
        }

        return CommandEnum.UNKNOWN;
    }

    private String type;

    private String name;

    private String handlerClassName;

    public String getType() {
        return type;
    }

    public String getName() {
        return name;
    }

    public String getHandlerClassName() {
        return handlerClassName;
    }
}

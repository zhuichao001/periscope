package com.jd.jim.testframework.executor.redis;

public interface RedisService {

    StringRedisService getStringRedisService();

    ListRedisService getListRedisService();

    DbRedisService getDbRedisService();

    HashRedisService getHashRedisService();

    SetRedisService getSetRedisService();

    SortedSetRedisService getSortedSetRedisService();

    HyperLogLogRedisService getHyperLogLogRedisService();

    BitRedisService getBitRedisService();

    ExpireRedisService getExpireRedisService();

    TransactionRedisService getTransactionRedisService();

    LuaRedisService getLuaRedisService();

    ClientServerRedisService getClientServerRedisService();

    DebugRedisService getDebugRedisService();

    InnerOrderRedisService getInnerOrderRedisService();

}

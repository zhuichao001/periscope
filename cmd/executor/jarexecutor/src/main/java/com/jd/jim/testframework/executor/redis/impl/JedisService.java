package com.jd.jim.testframework.executor.redis.impl;

import com.jd.jim.cli.exception.ScriptNotFoundException;
import com.jd.jim.testframework.executor.constant.CommonConstant;
import com.jd.jim.testframework.executor.enums.ObjectSubCommandEnum;
import com.jd.jim.testframework.executor.redis.*;
import com.jd.jim.testframework.executor.utils.CommonCollectionUtils;
import org.apache.commons.collections4.CollectionUtils;
import org.apache.commons.lang3.StringUtils;
import redis.clients.jedis.*;

import java.util.*;
import java.util.concurrent.TimeUnit;
import java.util.stream.Collectors;

public class JedisService implements RedisService {

    private final Jedis jedis;

    public JedisService(Jedis jedis) {
        this.jedis = jedis;
    }

    public Jedis getExecuteClient() {
        return jedis;
    }

    public StringRedisService getStringRedisService() {
        return this.new StringJedisServiceImpl();
    }

    public ListRedisService getListRedisService() {
        return this.new ListJedisServiceImpl();
    }

    public DbRedisService getDbRedisService() {
        return this.new DbJedisServiceImpl();
    }

    public HashRedisService getHashRedisService() {
        return this.new HashJedisServiceImpl();
    }

    public SetRedisService getSetRedisService() {
        return this.new SetJedisServiceImpl();
    }

    public SortedSetRedisService getSortedSetRedisService() {
        return this.new SortedSetJedisServiceImpl();
    }

    public HyperLogLogRedisService getHyperLogLogRedisService() {
        return this.new HyperLogLogJedisServiceImpl();
    }

    public BitRedisService getBitRedisService() {
        return this.new BitJedisServiceImpl();
    }

    public ExpireRedisService getExpireRedisService() {
        return this.new ExpireJedisServiceImpl();
    }

    public TransactionRedisService getTransactionRedisService() {
        return this.new TransactionJedisServiceImpl();
    }

    public LuaRedisService getLuaRedisService() {
        return this.new LuaJedisServiceImpl();
    }

    public ClientServerRedisService getClientServerRedisService() {
        return this.new ClientServerJedisServiceImpl();
    }

    public DebugRedisService getDebugRedisService() {
        return this.new DebugJedisServiceImpl();
    }

    public InnerOrderRedisService getInnerOrderRedisService() {
        return this.new InnerOrderJedisServiceImpl();
    }

    private class StringJedisServiceImpl implements StringRedisService {

        @Override
        public String set(String key, String value) {
            return getExecuteClient().set(key, value);
        }

        @Override
        public String get(String key) {

            return getExecuteClient().get(key);
        }

        @Override
        public String setNX(String key, String value) {
            Long sourceResult = getExecuteClient().setnx(key, value);
            return (null != sourceResult && sourceResult > 0) ? "true" : "false";
        }

        @Override
        public String setEx(String key, String value, long timeout, TimeUnit unit) {
            return getExecuteClient().setex(key, (int)timeout, value);
        }

        @Override
        public String strLen(String key) {
            Long sourceResult = getExecuteClient().strlen(key);
            return null == sourceResult ? "0" : sourceResult.toString();
        }

        @Override
        public String setRange(String key, String value, long offset) {
            Long sourceResult = getExecuteClient().setrange(key, offset, value);
            return null == sourceResult ? "0" : sourceResult.toString();
        }

        @Override
        public String psetex(String key, long milliseconds, String value) {
            return getExecuteClient().psetex(key, milliseconds, value);
        }

        @Override
        public String mset(List<String> paramsList) {
            String[] keyValue = paramsList.stream().toArray(String[]::new);

            return getExecuteClient().mset(keyValue);
        }

        @Override
        public String mget(String... keys) {
            List<String> values = getExecuteClient().mget(keys);

            StringBuilder temp = new StringBuilder();
            if (CollectionUtils.isNotEmpty(values)) {
                values.forEach(item -> {
                    temp.append(item).append(",");
                });
            }
            return temp.toString();
        }

        @Override
        public String decrBy(String key, long decrement) {
            Long value = getExecuteClient().decrBy(key, decrement);
            return value == null ? CommonConstant.ZERO : value.toString();
        }

        @Override
        public String getSet(String key, String value) {
            return getExecuteClient().getSet(key, value);
        }

        @Override
        public String append(String key, String value) {
            Long itemResult = getExecuteClient().append(key, value);
            return itemResult == null ? CommonConstant.ZERO : itemResult.toString();
        }

        @Override
        public String getRange(String key, long start, long end) {
            return getExecuteClient().getrange(key, start, end);
        }

        @Override
        public String incr(String key) {
            Long itemResult = getExecuteClient().incr(key);
            return itemResult == null ? CommonConstant.ZERO : itemResult.toString();
        }

        @Override
        public String incrBy(String key, long increment) {
            Long itemResult = getExecuteClient().incrBy(key, increment);
            return itemResult == null ? CommonConstant.ZERO : itemResult.toString();
        }

        @Override
        public String incrByFloat(String key, double increment) {
            Double itemResult = getExecuteClient().incrByFloat(key, increment);
            return itemResult == null ? CommonConstant.ZERO : itemResult.toString();
        }

        @Override
        public String decr(String key) {
            Long itemResult = getExecuteClient().decr(key);
            return itemResult == null ? CommonConstant.ZERO : itemResult.toString();
        }

        @Override
        public String msetnx(List<String> paramsList) {
            String[] keyValue = paramsList.stream().toArray(String[]::new);

            Long itemResult = getExecuteClient().msetnx(keyValue);
            return null == itemResult ? CommonConstant.ZERO : itemResult.toString();
        }
    }

    private class ListJedisServiceImpl implements ListRedisService {

        @Override
        public String lPush(String key, String... values) {
            Long result = getExecuteClient().lpush(key, values);
            return null == result ? CommonConstant.ZERO : result.toString();
        }

        @Override
        public String lPop(String key) {
            return getExecuteClient().lpop(key);
        }

        @Override
        public String lPushX(String key, String value) {
            Long result = getExecuteClient().lpushx(key, value);
            return null == result ? CommonConstant.ZERO : result.toString();
        }

        @Override
        public String rPush(String key, String... values) {
            Long result = getExecuteClient().rpush(key, values);
            return null == result ? CommonConstant.ZERO : result.toString();
        }

        @Override
        public String rPushX(String key, String value) {
            Long result = getExecuteClient().rpushx(key, value);
            return null == result ? CommonConstant.ZERO : result.toString();
        }

        @Override
        public String rPop(String key) {
            return getExecuteClient().rpop(key);
        }

        @Override
        public String rPopLPush(String source, String destination) {
            return getExecuteClient().rpoplpush(source, destination);
        }

        @Override
        public String lRem(String key, long count, String value) {
            Long result = getExecuteClient().lrem(key, count, value);
            return null == result ? CommonConstant.ZERO : result.toString();
        }

        @Override
        public String lLen(String key) {
            Long result = getExecuteClient().llen(key);
            return null == result ? CommonConstant.ZERO : result.toString();
        }

        @Override
        public String lIndex(String key, long index) {
            return getExecuteClient().lindex(key, index);
        }

        /**
         * lInsert
         * @param key
         * @param position
         * @param pivot
         * @param value
         * @return
         */
        @Override
        public String lInsert(String key, String position, String pivot, String value) {
            ListPosition position1 = ListPosition.valueOf(position);

            Long sourceResult = getExecuteClient().linsert(key, position1, pivot, value);
            return sourceResult == null ? CommonConstant.ZERO : sourceResult.toString();
        }

        @Override
        public String lSet(String key, long index, String value) {
            return getExecuteClient().lset(key, index, value);
        }

        @Override
        public String lRange(String key, long begin, long end) {
            return CommonCollectionUtils.list2String(getExecuteClient().lrange(key, begin, end));
        }

        @Override
        public String lTrim(String key, long begin, long end) {
            getExecuteClient().ltrim(key, begin, end);
            return CommonConstant.OK;
        }
    }

    private class DbJedisServiceImpl implements DbRedisService {

        /**
         * exists
         * @param key
         * @return
         */
        @Override
        public String exists(String key) {
            Boolean exists = getExecuteClient().exists(key);
            return (exists != null && exists) ? CommonConstant.TRUE : CommonConstant.FALSE;
        }

        /**
         * type
         * @param key
         * @return
         */
        @Override
        public String type(String key) {
            return getExecuteClient().type(key);
        }

        /**
         * rename
         * @param oldKey
         * @param newKey
         * @return
         */
        @Override
        public String rename(String oldKey, String newKey) {
            return getExecuteClient().rename(oldKey, newKey);
        }

        /**
         * renamenx
         * @param oldKey
         * @param newKey
         * @return
         */
        @Override
        public String renamenx(String oldKey, String newKey) {
            Long sourceResult = getExecuteClient().renamenx(oldKey, newKey);
            return sourceResult == null ? CommonConstant.ZERO : sourceResult.toString();
        }

        /**
         * move
         * @param key
         * @param db
         * @return
         */
        @Override
        public String move(String key, int db) {
            Long sourceResult = getExecuteClient().move(key, db);
            return sourceResult == null ? CommonConstant.ZERO : sourceResult.toString();
        }

        /**
         * del
         * @param key
         * @return
         */
        @Override
        public String del(String... key) {
            Long sourceResult = getExecuteClient().del(key);
            return null == sourceResult ? null : sourceResult.toString();
        }

        /**
         * randomKey
         * @return
         */
        @Override
        public String randomKey() {
            return getExecuteClient().randomKey();
        }

        /**
         * dbSize
         * @return
         */
        @Override
        public String dbSize() {
            Long sourceResult = getExecuteClient().dbSize();
            return null == sourceResult ? null : sourceResult.toString();
        }

        /**
         * keys
         * @param pattern
         * @return
         */
        @Override
        public String keys(String pattern) {
            Set<String> sourceResult = getExecuteClient().keys(pattern);
            return CommonCollectionUtils.set2String(sourceResult);
        }

        /**
         * TODO 支持 pattern 与 count
         * hscan
         * @param commandList
         * @return
         */
        @Override
        public String scan(List<String> commandList) {
            String cursor = commandList.get(0);

            ScanResult<String> sourceResult = getExecuteClient().scan(cursor);
            return CommonCollectionUtils.scanResult2String(sourceResult);
        }

        /**
         * sort
         * @param key
         * @return
         */
        @Override
        public String sort(String key) {
            List<String> sourceResult = new ArrayList<>(getExecuteClient().sort(key));
            return CommonCollectionUtils.list2String(sourceResult);
        }

        /**
         * flushDB
         * @return
         */
        @Override
        public String flushDB() {
            return getExecuteClient().flushDB();
        }

        /**
         * flushAll
         * @return
         */
        @Override
        public String flushAll() {
            return getExecuteClient().flushAll();
        }

        /**
         * select
         * @param index
         * @return
         */
        @Override
        public String select(int index) {
            return getExecuteClient().select(index);
        }

        /**
         * swapDB
         * @param index1
         * @param index2
         * @return
         */
        @Override
        public String swapDB(int index1, int index2) {
            return getExecuteClient().swapDB(index1, index2);
        }
    }

    private class HashJedisServiceImpl implements HashRedisService {

        /**
         * hset
         * @parma hash
         * @param field
         * @param value
         * @return
         */
        @Override
        public String hset(String key, String field, String value) {
            Long sourceResult = getExecuteClient().hset(key, field, value);
            return sourceResult == null ? CommonConstant.ZERO : sourceResult.toString();
        }

        /**
         * hsetnx
         * @param key
         * @param field
         * @param value
         * @return
         */
        @Override
        public String hsetnx(String key, String field, String value) {
            Long sourceResult = getExecuteClient().hsetnx(key, field, value);
            return sourceResult == null ? CommonConstant.ZERO : sourceResult.toString();
        }

        /**
         * hget
         * @param key
         * @param field
         * @return
         */
        @Override
        public String hget(String key, String field) {
            return getExecuteClient().hget(key, field);
        }

        /**
         * hexists
         * @param key
         * @param field
         * @return
         */
        @Override
        public String hexists(String key, String field) {
            Boolean sourceResult = getExecuteClient().hexists(key, field);
            return sourceResult == null ? CommonConstant.FALSE : sourceResult.toString();
        }

        /**
         * hdel
         * @param key
         * @param field
         * @return
         */
        @Override
        public String hdel(String key, String... field) {
            Long sourceResult = getExecuteClient().hdel(key, field);
            return sourceResult == null ? CommonConstant.ZERO : sourceResult.toString();
        }

        /**
         * hlen
         * @param key
         * @return
         */
        @Override
        public String hlen(String key) {
            Long sourceResult = getExecuteClient().hlen(key);
            return sourceResult == null ? CommonConstant.ZERO : sourceResult.toString();
        }

        /**
         * hstrlen
         * @param key
         * @param field
         * @return
         */
        @Override
        public String hstrlen(String key, String field) {
            Long sourceResult = getExecuteClient().hstrlen(key, field);
            return sourceResult == null ? CommonConstant.ZERO : sourceResult.toString();
        }

        /**
         * hincrby
         * @param key
         * @param field
         * @param delta
         * @return
         */
        @Override
        public String hincrBy(String key, String field, long delta) {
            Long sourceResult = getExecuteClient().hincrBy(key, field, delta);
            return sourceResult == null ? CommonConstant.ZERO : sourceResult.toString();
        }

        /**
         * hincrbyfloat
         * @param key
         * @param field
         * @param delta
         * @return
         */
        @Override
        public String hincrByFloat(String key, String field, double delta) {
            Double sourceResult = getExecuteClient().hincrByFloat(key, field, delta);
            return sourceResult == null ? CommonConstant.ZERO : sourceResult.toString();
        }

        /**
         * hmset
         * @param key
         * @param hash
         * @return
         */
        @Override
        public String hmset(String key, Map<String, String> hash) {
            return getExecuteClient().hmset(key, hash);
        }

        /**
         * hmget
         * @param key
         * @param fields
         * @return
         */
        @Override
        public String hmget(String key, String... fields) {
            List<String> sourceResult = getExecuteClient().hmget(key, fields);
            return CommonCollectionUtils.list2String(sourceResult);
        }

        /**
         * hkeys
         * @param key
         * @return
         */
        @Override
        public String hkeys(String key) {
            Set<String> sourceResult = getExecuteClient().hkeys(key);
            return CommonCollectionUtils.set2String(sourceResult);
        }

        /**
         * hvals
         * @param key
         * @return
         */
        @Override
        public String hvals(String key) {
            List<String> sourceResult = getExecuteClient().hvals(key);
            return CommonCollectionUtils.list2String(sourceResult);
        }

        /**
         * hgetAll
         * @return
         */
        @Override
        public String hgetAll(String key) {
            Map<String, String> sourceResult = getExecuteClient().hgetAll(key);
            return CommonCollectionUtils.map2String(sourceResult);
        }

        /**
         * hscanMatchCount
         * @param key
         * @param cursor
         * @param params
         * @return
         */
        @Override
        public String hscan(String key, String cursor, Map<String, String> params) {
            ScanParams scanParams = new ScanParams();

            if (params.containsKey(CommonConstant.MATCH)) {
                scanParams.match(params.get(CommonConstant.MATCH));
            }

            if (params.containsKey(CommonConstant.COUNT)) {
                scanParams.count(Integer.valueOf(params.get(CommonConstant.COUNT)));
            }

            ScanResult<Map.Entry<String, String>> sourceResult =
                    getExecuteClient().hscan(key, cursor, scanParams);

            return CommonCollectionUtils.scanResult2String(sourceResult);
        }

    }

    private class SetJedisServiceImpl implements SetRedisService {

        @Override
        public String sAdd(String key, String... values) {
            Long result = getExecuteClient().sadd(key, values);
            return null == result ? CommonConstant.ZERO : result.toString();
        }

        @Override
        public String sIsMember(String key, String value) {
            Boolean result = getExecuteClient().sismember(key, value);
            return null == result ? CommonConstant.FALSE : result.toString();
        }

        @Override
        public String sPop(String key) {
            return getExecuteClient().spop(key);
        }

        @Override
        public String sRandMember(String key, Long count) {
            return null == count ? getExecuteClient().srandmember(key)
                    : CommonCollectionUtils.list2String(getExecuteClient().srandmember(key, count.intValue()));
        }

        @Override
        public String sRem(String key, String... values) {
            Long result = getExecuteClient().srem(key, values);
            return null == result ? CommonConstant.ZERO : result.toString();
        }

        @Override
        public String sMove(String source, String destination, String value) {
            Long result = getExecuteClient().smove(source, destination, value);
            return null == result ? CommonConstant.FALSE : result.toString();
        }

        @Override
        public String sCard(String key) {
            Long result = getExecuteClient().scard(key);
            return null == result ? CommonConstant.ZERO : result.toString();
        }

        @Override
        public String sMembers(String key) {
            return CommonCollectionUtils.set2String(getExecuteClient().smembers(key));
        }

        @Override
        public String sscan(String key, String cursor, Map<String, String> params) {
            ScanParams scanParams = new ScanParams();

            if (params.containsKey(CommonConstant.MATCH)) {
                scanParams.match(params.get(CommonConstant.MATCH));
            }

            if (params.containsKey(CommonConstant.COUNT)) {
                scanParams.count(Integer.valueOf(CommonConstant.COUNT));
            }

            ScanResult<String> scanResult = getExecuteClient().sscan(key, cursor, scanParams);

            return CommonCollectionUtils.scanResult2String(scanResult);
        }

        @Override
        public String sInter(String... keys) {
            return CommonCollectionUtils.set2String(getExecuteClient().sinter(keys));
        }

        @Override
        public String sInterStore(String destination, String... keys) {
            Long result = getExecuteClient().sinterstore(destination, keys);
            return null == result ? CommonConstant.ZERO : result.toString();
        }

        @Override
        public String sUnion(String... keys) {
            return CommonCollectionUtils.set2String(getExecuteClient().sunion(keys));
        }

        @Override
        public String sUnionStore(String destination, String... keys) {
            Long result = getExecuteClient().sunionstore(destination, keys);
            return null == result ? CommonConstant.ZERO : result.toString();
        }

        @Override
        public String sDiff(String... keys) {
            return CommonCollectionUtils.set2String(getExecuteClient().sdiff(keys));
        }

        @Override
        public String sDiffStore(String destination, String... keys) {
            Long result = getExecuteClient().sdiffstore(destination, keys);
            return null == result ? CommonConstant.ZERO : result.toString();
        }
    }

    private class SortedSetJedisServiceImpl implements SortedSetRedisService {

        /**
         * zadd
         * @parma key
         * @param score
         * @param member
         */
        @Override
        public String zadd(String key, double score, String member) {
            Long sourceResult = getExecuteClient().zadd(key, score, member);
            return sourceResult == null ? CommonConstant.ZERO : sourceResult.toString();
        }

        /**
         * zscore
         * @param key
         * @param member
         * @return
         */
        @Override
        public String zscore(String key, String member) {
            Double sourceResult = getExecuteClient().zscore(key, member);
            return sourceResult == null ? CommonConstant.ZERO : sourceResult.toString();
        }

        /**
         * zincrBy
         * @param key
         * @param delta
         * @param member
         * @return
         */
        @Override
        public String zincrBy(String key, double delta, String member) {
            Double sourceResult = getExecuteClient().zincrby(key, delta, member);
            return sourceResult == null ? CommonConstant.ZERO : sourceResult.toString();
        }

        /**
         * zcard
         * @param key
         * @return
         */
        @Override
        public String zcard(String key) {
            Long sourceResult = getExecuteClient().zcard(key);
            return sourceResult == null ? CommonConstant.ZERO : sourceResult.toString();
        }

        /**
         * zcount
         * @param key
         * @param min
         * @param max
         * @return
         */
        @Override
        public String zcount(String key, double min, double max) {
            Long sourceResult = getExecuteClient().zcount(key, min, max);
            return sourceResult == null ? CommonConstant.ZERO : sourceResult.toString();
        }

        /**
         * zrange
         * @param key
         * @param start
         * @param stop
         * @return
         */
        @Override
        public String zrange(String key, long start, long stop) {
            Set<String> sourceResult = getExecuteClient().zrange(key, start, stop);
            return CommonCollectionUtils.set2String(sourceResult);
        }

        /**
         * zrevrange
         * @param key
         * @param start
         * @param stop
         * @return
         */
        @Override
        public String zrevrange(String key, long start, long stop) {
            Set<String> sourceResult = getExecuteClient().zrevrange(key, start, stop);
            return CommonCollectionUtils.set2String(sourceResult);
        }

        /**
         * zrangebyscore
         * @param key
         * @param min
         * @param max
         * @return
         */
        @Override
        public String zrangeByScore(String key, double min, double max) {
            Set<String> sourceResult = getExecuteClient().zrangeByScore(key, min, max);
            return CommonCollectionUtils.set2String(sourceResult);
        }

        /**
         * zrangebyscore
         * @param key
         * @param min
         * @param max
         * @return
         */
        @Override
        public String zrangeByScore(String key, String min, String max) {
            Set<String> sourceResult = getExecuteClient().zrangeByScore(key, min, max);
            return CommonCollectionUtils.set2String(sourceResult);
        }

        /**
         * zrevrangebyscore
         * @param key
         * @param max
         * @param min
         * @return
         */
        @Override
        public String zrevrangeByScore(String key, double max, double min) {
            Set<String> sourceResult = getExecuteClient().zrevrangeByScore(key, max, min);
            return CommonCollectionUtils.set2String(sourceResult);
        }

        /**
         * zrevrangebyscore
         * @param key
         * @param max
         * @param min
         * @return
         */
        @Override
        public String zrevrangeByScore(String key, String max, String min) {
            Set<String> sourceResult = getExecuteClient().zrevrangeByScore(key, max, min);
            return CommonCollectionUtils.set2String(sourceResult);
        }

        /**
         * zrank
         * @param key
         * @param member
         * @return
         */
        @Override
        public String zrank(String key, String member) {
            Long sourceResult = getExecuteClient().zrank(key, member);
            return sourceResult == null ? CommonConstant.ZERO : sourceResult.toString();
        }

        /**
         *
         * @param key
         * @param member
         * @return
         */
        @Override
        public String zrevrank(String key, String member) {
            Long sourceResult = getExecuteClient().zrevrank(key, member);
            return sourceResult == null ? CommonConstant.ZERO : sourceResult.toString();
        }

        /**
         *
         * @param key
         * @param member
         * @return
         */
        @Override
        public String zrem(String key, String... member) {
            Long sourceResult = getExecuteClient().zrem(key, member);
            return sourceResult == null ? CommonConstant.ZERO : sourceResult.toString();
        }

        /**
         *
         * @param key
         * @param start
         * @param stop
         * @return
         */
        @Override
        public String zremrangeByRank(String key, long start, long stop) {
            Long sourceResult = getExecuteClient().zremrangeByRank(key, start, stop);
            return sourceResult == null ? CommonConstant.ZERO : sourceResult.toString();
        }

        /**
         * zremrangeByScore
         * @param key
         * @param min
         * @param max
         * @return
         */
        @Override
        public String zremrangeByScore(String key, double min, double max) {
            Long sourceResult = getExecuteClient().zremrangeByScore(key, min, max);
            return sourceResult == null ? CommonConstant.ZERO : sourceResult.toString();
        }

        /**
         * zremrangeByScore
         * @param key
         * @param min
         * @param max
         * @return
         */
        @Override
        public String zremrangeByScore(String key, String min, String max) {
            Long sourceResult = getExecuteClient().zremrangeByScore(key, min, max);
            return sourceResult == null ? CommonConstant.ZERO : sourceResult.toString();
        }

        /**
         * zrangeByLex
         * @param key
         * @param min
         * @param max
         * @return
         */
        @Override
        public String zrangeByLex(String key, String min, String max) {
            Set<String> sourceResult = getExecuteClient().zrangeByLex(key, min, max);
            return CommonCollectionUtils.set2String(sourceResult);
        }

        /**
         * zlexcount
         * @param key
         * @param min
         * @param max
         * @return
         */
        @Override
        public String zlexcount(String key, String min, String max) {
            Long sourceResult = getExecuteClient().zlexcount(key, min, max);
            return sourceResult == null ? CommonConstant.ZERO : sourceResult.toString();
        }

        /**
         * zremrangeByLex
         * @param key
         * @param min
         * @param max
         * @return
         */
        @Override
        public String zremrangeByLex(String key, String min, String max) {
            Long sourceResult = getExecuteClient().zremrangeByLex(key, min, max);
            return sourceResult == null ? CommonConstant.ZERO : sourceResult.toString();
        }

        /**
         * zscan
         * @param key
         * @param cursor
         * @param params
         * @return
         */
        @Override
        public String zscan(String key, String cursor, Map<String, String> params) {

            ScanParams scanParams = new ScanParams();
            if (params.containsKey(CommonConstant.MATCH)) {
                scanParams.match(params.get(CommonConstant.MATCH));
            }
            if (params.containsKey(CommonConstant.COUNT)) {
                scanParams.count(Integer.valueOf(params.get(CommonConstant.COUNT)));
            }

            ScanResult<Tuple> sourceResult = getExecuteClient().zscan(key, cursor, scanParams);
            return CommonCollectionUtils.scanResult2String(sourceResult);
        }
        /**
         * zunionstore
         * @param destination
         * @param sets
         * @return
         */
        @Override
        public String zunionstore(String destination, String... sets) {
            Long sourceResult = getExecuteClient().zunionstore(destination, sets);
            return sourceResult == null ? CommonConstant.ZERO : sourceResult.toString();
        }

        /**
         * zinterstore
         * @param destination
         * @param sets
         * @return
         */
        @Override
        public String zinterstore(String destination, String... sets) {
            Long sourceResult = getExecuteClient().zinterstore(destination, sets);
            return sourceResult == null ? CommonConstant.ZERO : sourceResult.toString();
        }
    }

    private class HyperLogLogJedisServiceImpl implements HyperLogLogRedisService {

        /**
         * pfadd
         * @parma key
         * @param element
         * @return
         */
        @Override
        public String pfadd(String key, String... element) {
            Long sourceResult = getExecuteClient().pfadd(key, element);
            return sourceResult == null ? CommonConstant.ZERO : sourceResult.toString();
        }

        /**
         * pfcount
         * @parma key
         * @return
         */
        @Override
        public String pfcount(String key) {
            Long sourceResult = getExecuteClient().pfcount(key);
            return sourceResult == null ? CommonConstant.ZERO : sourceResult.toString();
        }

        /**
         * pfmerge
         * @param destkey
         * @param sourcekey
         * @return
         */
        @Override
        public String pfmerge(String destkey, String... sourcekey) {
            return getExecuteClient().pfmerge(destkey, sourcekey);
        }
    }

    private class BitJedisServiceImpl implements BitRedisService {

        /**
         * setbit
         * @param key
         * @param offset
         * @param value
         * @return
         */
        @Override
        public String setbit(String key, long offset, boolean value) {
            Boolean sourceResult = getExecuteClient().setbit(key, offset, value);
            return sourceResult == null ? CommonConstant.FALSE : sourceResult.toString();
        }

        /**
         * getbit
         * @param key
         * @param offset
         * @return
         */
        @Override
        public String getbit(String key, long offset) {
            Boolean sourceResult = getExecuteClient().getbit(key, offset);
            return sourceResult == null ? CommonConstant.FALSE : sourceResult.toString();
        }

        /**
         * bitcount
         * @param key
         * @return
         */
        @Override
        public String bitcount(String key) {
            Long sourceResult = getExecuteClient().bitcount(key);
            return sourceResult == null ? CommonConstant.ZERO: sourceResult.toString();
        }

        /**
         * bitcount
         * @param key
         * @param start
         * @param end
         * @return
         */
        @Override
        public String bitcount(String key, long start, long end) {
            Long sourceResult = getExecuteClient().bitcount(key, start, end);
            return sourceResult == null ? CommonConstant.ZERO: sourceResult.toString();
        }

        /**
         * bitpos
         * @param key
         * @return
         */
        @Override
        public String bitpos(String key, boolean bit) {
            Long sourceResult = getExecuteClient().bitpos(key, bit);
            return sourceResult == null ? CommonConstant.ZERO: sourceResult.toString();
        }

        /**
         * bitop
         * @param commandList
         * @return
         */
        @Override
        public String bitop(List<String> commandList) {
            BitOP bitOP = BitOP.valueOf(commandList.get(0));
            String destKey = commandList.get(1);
            String[] sourceKeys = commandList.subList(2, commandList.size())
                    .toArray(new String[0]);

            Long sourceResult = getExecuteClient().bitop(bitOP, destKey, sourceKeys);
            return sourceResult == null ? CommonConstant.ZERO: sourceResult.toString();
        }

        /**
         * bitop
         * @param commandList
         * @return
         */
        @Override
        public String bitfield(List<String> commandList) {
            String key = commandList.get(0);
            String[] arguments = commandList.subList(1, commandList.size())
                    .toArray(new String[0]);

            List<Long> sourceResult = getExecuteClient().bitfield(key, arguments);
            return longListToString(sourceResult);
        }

        private String longListToString(List<Long> list) {
            return list.stream()
                    .map(i -> i==null ? CommonConstant.ZERO : i.toString())
                    .collect(Collectors.joining(","));
        }
    }

    private class ExpireJedisServiceImpl implements ExpireRedisService {

        /**
         * expire
         * @param key
         * @param timeout
         * @param unit
         * @return
         */
        @Override
        public String expire(String key, long timeout, TimeUnit unit) {
            Long sourceResult = getExecuteClient().expire(key, (int) timeout);
            return (null != sourceResult && sourceResult > 0) ? "true" : "false";
        }

        /**
         * expireAt
         * @param key
         * @param unixTime
         * @return
         */
        @Override
        public String expireAt(String key, long unixTime) {
            Long sourceResult = getExecuteClient().expireAt(key, unixTime);
            return (null != sourceResult && sourceResult > 0) ? "true" : "false";
        }

        /**
         * ttl
         * @param key
         * @return
         */
        @Override
        public String ttl(String key) {
            Long sourceResult = getExecuteClient().ttl(key);
            return (null != sourceResult && sourceResult > 0) ? "true" : "false";
        }

        @Override
        public String persist(String key) {
            Long sourceResult = getExecuteClient().persist(key);
            return (null != sourceResult && sourceResult > 0) ? "true" : "false";
        }

        /**
         * pexpire
         * @param key
         * @param milliseconds
         * @return
         */
        @Override
        public String pexpire(String key, long milliseconds) {
            Long sourceResult = getExecuteClient().pexpire(key, milliseconds);
            return (null != sourceResult && sourceResult > 0) ? "true" : "false";
        }

        /**
         * pexpireAt
         * @param key
         * @param millisecondUnixTime
         * @return
         */
        @Override
        public String pexpireAt(String key, long millisecondUnixTime) {
            Long sourceResult = getExecuteClient().pexpireAt(key, millisecondUnixTime);
            return (null != sourceResult && sourceResult > 0) ? "true" : "false";
        }

        /**
         * pttl
         * @param key
         * @return
         */
        @Override
        public String pttl(String key) {
            Long sourceResult = getExecuteClient().pttl(key);
            return (null != sourceResult && sourceResult > 0) ? "true" : "false";
        }
    }

    private class TransactionJedisServiceImpl implements TransactionRedisService {

        public String multi() {
            getExecuteClient().multi();
            return CommonConstant.OK;
        }
    }

    private class LuaJedisServiceImpl implements LuaRedisService {

        @Override
        public String eval(String script, List<String> keys, List<String> args) {
            Object itemResult = getExecuteClient().eval(script, keys, args);
            return itemResult == null ? CommonConstant.EMPTY : itemResult.toString();
        }

        @Override
        public String evalsha(String sha, List<String> keys, List<String> args) throws ScriptNotFoundException {
            Object object = getExecuteClient().evalsha(sha, keys, args);
            return null == object ? CommonConstant.EMPTY : object.toString();
        }
    }

    private class ClientServerJedisServiceImpl implements ClientServerRedisService {

        @Override
        public String auth(String password) {
            return getExecuteClient().auth(password);
        }

    }

    private class DebugJedisServiceImpl implements DebugRedisService {

        @Override
        public String ping() {
            return getExecuteClient().ping();
        }

        @Override
        public String ping(String message) {
            return StringUtils.isEmpty(message) ? getExecuteClient().ping() : getExecuteClient().ping(message);
        }

        @Override
        public String echo(String str) {
            return getExecuteClient().echo(str);
        }

        @Override
        public String object(String subCommand, String key) {
            if (ObjectSubCommandEnum.ENCODING.equals(subCommand)) {
                return getExecuteClient().objectEncoding(key);
            } else if (ObjectSubCommandEnum.IDLETIME.equals(subCommand)) {
                Long itemResult = getExecuteClient().objectIdletime(key);
                return null == itemResult ? CommonConstant.ZERO : itemResult.toString();
            } else if (ObjectSubCommandEnum.REFCOUNT.equals(subCommand)) {
                Long itemResult = getExecuteClient().objectRefcount(key);
                return null == itemResult ? CommonConstant.ZERO : itemResult.toString();
            }

            return "";
        }
    }

    private class InnerOrderJedisServiceImpl implements InnerOrderRedisService {

        @Override
        public String dump(String key) {
            byte[] result = getExecuteClient().dump(key);
            return null == result ? CommonConstant.EMPTY : new String(result);
        }

        @Override
        public String restore(String key, long ttl, byte[] serializedValue) {
            return getExecuteClient().restore(key, Long.valueOf(ttl).intValue(), serializedValue);
        }
    }

}

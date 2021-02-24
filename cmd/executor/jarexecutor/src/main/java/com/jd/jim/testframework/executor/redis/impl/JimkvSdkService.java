package com.jd.jim.testframework.executor.redis.impl;

import com.google.common.collect.Maps;
import com.google.protobuf.ByteString;
import com.jd.jim.cli.Cluster;
import com.jd.jim.cli.exception.ScriptNotFoundException;
import com.jd.jim.cli.protocol.*;
import com.jd.jim.testframework.executor.constant.CommonConstant;
import com.jd.jim.testframework.executor.enums.ObjectSubCommandEnum;
import com.jd.jim.testframework.executor.redis.*;
import com.jd.jim.testframework.executor.utils.CommonCollectionUtils;
import org.apache.commons.collections4.CollectionUtils;

import java.util.*;
import java.util.concurrent.TimeUnit;

public class JimkvSdkService implements RedisService {

    private final Cluster jimDbClient;

    public JimkvSdkService(Cluster jimDbClient) {
        this.jimDbClient = jimDbClient;
    }

    protected Cluster getExecuteClient() {
        return jimDbClient;
    }

    public StringRedisService getStringRedisService() {
        return this.new StringJimkvSdkServiceImpl();
    }

    public ListRedisService getListRedisService() {
        return this.new ListJimkvSdkServiceImpl();
    }

    public DbRedisService getDbRedisService() {
        return this.new DbJimkvSdkServiceImpl();
    }

    public HashRedisService getHashRedisService() {
        return this.new HashJimkvSdkServiceImpl();
    }

    public SetRedisService getSetRedisService() {
        return this.new SetJimkvSdkServiceImpl();
    }

    public SortedSetRedisService getSortedSetRedisService() {
        return this.new SortedSetJimkvSdkServiceImpl();
    }

    public HyperLogLogRedisService getHyperLogLogRedisService() {
        return this.new HyperLogLogJimkvSdkServiceImpl();
    }

    public BitRedisService getBitRedisService() {
        return this.new BitJimkvSdkServiceImpl();
    }

    public ExpireRedisService getExpireRedisService() {
        return this.new ExpireJimkvSdkServiceImpl();
    }

    public TransactionRedisService getTransactionRedisService() {
        return this.new TransactionJimkvSdkServiceImpl();
    }

    public LuaRedisService getLuaRedisService() {
        return this.new LuaJimkvSdkServiceImpl();
    }

    public ClientServerRedisService getClientServerRedisService() {
        return this.new ClientServerJimkvSdkServiceImpl();
    }

    public DebugRedisService getDebugRedisService() {
        return this.new DebugJimkvSdkServiceImpl();
    }

    public InnerOrderRedisService getInnerOrderRedisService() {
        return this.new InnerOrderJimkvSdkServiceImpl();
    }

    /**
     * BitRedisService
     */
    private class BitJimkvSdkServiceImpl implements BitRedisService {

        /**
         * setbit
         * @param key
         * @param offset
         * @param value
         * @return
         */
        @Override
        public String setbit(String key, long offset, boolean value) {
            Boolean sourceResult = getExecuteClient().setBit(key, offset, value);
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
            Boolean sourceResult = getExecuteClient().getBit(key, offset);
            return sourceResult == null ? CommonConstant.FALSE : sourceResult.toString();
        }

        /**
         * bitcount
         * @param key
         * @return
         */
        @Override
        public String bitcount(String key) {
            Long sourceResult = getExecuteClient().bitCount(key);
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
            Long sourceResult = getExecuteClient().bitCount(key, start, end);
            return sourceResult == null ? CommonConstant.ZERO: sourceResult.toString();
        }

        /**
         * TODO 暂时不支持此方法
         * bitpos
         * @param key
         * @return
         */
        @Override
        public String bitpos(String key, boolean bit) {
            throw new UnsupportedOperationException(String.format(CommonConstant.UN_SUPPORT_PREFIX, "bitPos"));
        }

        /**
         * bitop
         * @param commandList
         * @return
         */
        @Override
        public String bitop(List<String> commandList) {
            BitOperation bitOperation = BitOperation.valueOf(commandList.get(0));
            String destKey = commandList.get(1);
            String[] sourceKeys = commandList.subList(2, commandList.size())
                    .toArray(new String[0]);

            Long sourceResult = getExecuteClient().bitOp(bitOperation, destKey, sourceKeys);
            return sourceResult == null ? CommonConstant.ZERO: sourceResult.toString();
        }

        /**
         * TODO 暂时不支持此方法
         * bitop
         * @param commandList
         * @return
         */
        @Override
        public String bitfield(List<String> commandList) {
            throw new UnsupportedOperationException(String.format(CommonConstant.UN_SUPPORT_PREFIX, "bitField"));
        }
    }

    /**
     * ClientServerRedisService
     */
    private class ClientServerJimkvSdkServiceImpl implements ClientServerRedisService {

        @Override
        public String auth(String password) {
            throw new UnsupportedOperationException(String.format(CommonConstant.UN_SUPPORT_PREFIX, "auth"));
        }
    }

    /**
     * DbRedisService
     */
    private class DbJimkvSdkServiceImpl implements DbRedisService {

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
            return getExecuteClient().type(key).name();
        }

        /**
         * rename
         * @param oldKey
         * @param newKey
         * @return
         */
        @Override
        public String rename(String oldKey, String newKey) {
            getExecuteClient().rename(oldKey, newKey);
            return CommonConstant.OK;
        }

        /**
         * renamenx
         * @param oldKey
         * @param newKey
         * @return
         */
        @Override
        public String renamenx(String oldKey, String newKey) {
            Boolean sourceResult = getExecuteClient().renameNX(oldKey, newKey);
            return sourceResult == null ? CommonConstant.FALSE : sourceResult.toString();
        }

        /**
         * TODO 暂时不支持该方法
         * move
         * @param key
         * @param db
         * @return
         */
        @Override
        public String move(String key, int db) {
            throw new UnsupportedOperationException(String.format(CommonConstant.UN_SUPPORT_PREFIX, "move"));
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
         * TODO 暂时不支持该方法
         * randomKey
         * @return
         */
        @Override
        public String randomKey() {
            throw new UnsupportedOperationException(String.format(CommonConstant.UN_SUPPORT_PREFIX, "randomKey"));
        }

        /**
         * TODO 暂时不支持该方法
         * dbSize
         * @return
         */
        @Override
        public String dbSize() {
            throw new UnsupportedOperationException(String.format(CommonConstant.UN_SUPPORT_PREFIX, "dbSize"));
        }

        /**
         * TODO 暂时不支持该方法
         * keys
         * @param pattern
         * @return
         */
        @Override
        public String keys(String pattern) {
            throw new UnsupportedOperationException(String.format(CommonConstant.UN_SUPPORT_PREFIX, "keys"));
        }

        /**
         * TODO 支持 pattern 与 count
         * hscan
         * @param commandList
         * @return
         */
        @Override
        public String scan(List<String> commandList) {
            ByteString cursor = ByteString.copyFromUtf8(commandList.get(0));
            ScanOptions scanOptions = ScanOptions.scanOptions().build();

            KeyScanResult<String> sourceResult = getExecuteClient().scan(cursor, scanOptions);
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
         * TODO 暂时不支持该方法
         * flushDB
         * @return
         */
        @Override
        public String flushDB() {
            throw new UnsupportedOperationException(String.format(CommonConstant.UN_SUPPORT_PREFIX, "flushDB"));
        }

        /**
         * TODO 暂时不支持该方法
         * flushAll
         * @return
         */
        @Override
        public String flushAll() {
            throw new UnsupportedOperationException(String.format(CommonConstant.UN_SUPPORT_PREFIX, "flushAll"));
        }

        /**
         * TODO 暂时不支持该方法
         * select
         * @param index
         * @return
         */
        @Override
        public String select(int index) {
            throw new UnsupportedOperationException(String.format(CommonConstant.UN_SUPPORT_PREFIX, "select"));
        }

        /**
         * TODO 暂时不支持该方法
         * swapDB
         * @param index1
         * @param index2
         * @return
         */
        @Override
        public String swapDB(int index1, int index2) {
            throw new UnsupportedOperationException(String.format(CommonConstant.UN_SUPPORT_PREFIX, "swapDB"));
        }
    }

    /**
     * DebugRedisService
     */
    private class DebugJimkvSdkServiceImpl implements DebugRedisService {

        @Override
        public String ping() {
            throw new UnsupportedOperationException(String.format(CommonConstant.UN_SUPPORT_PREFIX, "ping"));
        }

        @Override
        public String ping(String message) {
            throw new UnsupportedOperationException(String.format(CommonConstant.UN_SUPPORT_PREFIX, "ping"));
        }

        @Override
        public String echo(String str) {
            throw new UnsupportedOperationException(String.format(CommonConstant.UN_SUPPORT_PREFIX, "echo"));
        }

        @Override
        public String object(String subCommand, String key) {
            if (ObjectSubCommandEnum.IDLETIME.equals(subCommand)) {
                Long itemResult = getExecuteClient().objectIdletime(key);
                return null == itemResult ? CommonConstant.ZERO : itemResult.toString();
            } else {
                throw new UnsupportedOperationException(String.format(String.format(CommonConstant.UN_SUPPORT_PREFIX, "command object:" + subCommand)));
            }
        }
    }

    /**
     * ExpireRedisService
     */
    private class ExpireJimkvSdkServiceImpl implements ExpireRedisService {

        /**
         * expire
         * @param key
         * @param timeout
         * @param unit
         * @return
         */
        @Override
        public String expire(String key, long timeout, TimeUnit unit) {
            Boolean sourceResult = getExecuteClient().expire(key, timeout, unit);
            return null == sourceResult ? CommonConstant.FALSE: sourceResult.toString();
        }

        /**
         * expireAt
         * @param key
         * @param unixTime
         * @return
         */
        @Override
        public String expireAt(String key, long unixTime) {
            Date date = new Date(unixTime);

            Boolean sourceResult = getExecuteClient().expireAt(key, date);
            return null == sourceResult ? CommonConstant.FALSE: sourceResult.toString();
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
            Boolean sourceResult = getExecuteClient().persist(key);
            return null == sourceResult ? CommonConstant.FALSE : sourceResult.toString();
        }

        /**
         * expire
         * @param key
         * @param milliseconds
         * @return
         */
        @Override
        public String pexpire(String key, long milliseconds) {
            Boolean sourceResult = getExecuteClient().pExpire(key, milliseconds, TimeUnit.MILLISECONDS);
            return null == sourceResult ? CommonConstant.FALSE: sourceResult.toString();
        }

        /**
         * pexpireAt
         * @param key
         * @param millisecondUnixTime
         * @return
         */
        @Override
        public String pexpireAt(String key, long millisecondUnixTime) {
            Date date = new Date(millisecondUnixTime);

            Boolean sourceResult = getExecuteClient().pExpireAt(key, date);
            return null == sourceResult ? CommonConstant.FALSE: sourceResult.toString();
        }

        /**
         * pttl
         * @param key
         * @return
         */
        @Override
        public String pttl(String key) {
            Long sourceResult = getExecuteClient().pTtl(key);
            return (null != sourceResult && sourceResult > 0) ? "true" : "false";
        }
    }

    /**
     * HashRedisService
     */
    private class HashJimkvSdkServiceImpl implements HashRedisService {

        /**
         * hset
         * @parma hash
         * @param field
         * @param value
         * @return
         */
        @Override
        public String hset(String key, String field, String value) {
            Boolean sourceResult = getExecuteClient().hSet(key, field, value);
            return sourceResult == null ? CommonConstant.FALSE : sourceResult.toString();
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
            Boolean sourceResult = getExecuteClient().hSetNX(key, field, value);
            return sourceResult == null ? CommonConstant.FALSE : sourceResult.toString();
        }

        /**
         * hget
         * @param key
         * @param field
         * @return
         */
        @Override
        public String hget(String key, String field) {
            return getExecuteClient().hGet(key, field);
        }

        /**
         * hexists
         * @param key
         * @param field
         * @return
         */
        @Override
        public String hexists(String key, String field) {
            Boolean sourceResult = getExecuteClient().hExists(key, field);
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
            Long sourceResult = getExecuteClient().hDel(key, field);
            return sourceResult == null ? CommonConstant.ZERO : sourceResult.toString();
        }

        /**
         * hlen
         * @param key
         * @return
         */
        @Override
        public String hlen(String key) {
            Long sourceResult = getExecuteClient().hLen(key);
            return sourceResult == null ? CommonConstant.ZERO : sourceResult.toString();
        }

        /**
         * TODO 暂时不支持
         * hstrlen
         * @param key
         * @param field
         * @return
         */
        @Override
        public String hstrlen(String key, String field) {
            throw new UnsupportedOperationException(String.format(CommonConstant.UN_SUPPORT_PREFIX, "hStrLen"));
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
            Long sourceResult = getExecuteClient().hIncrBy(key, field, delta);
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
            Double sourceResult = getExecuteClient().hIncrBy(key, field, delta);
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
            getExecuteClient().hMSet(key, hash);
            return CommonConstant.OK;
        }

        /**
         * hmget
         * @param key
         * @param fields
         * @return
         */
        @Override
        public String hmget(String key, String... fields) {
            List<String> sourceResult = getExecuteClient().hMGet(key, fields);
            return CommonCollectionUtils.list2String(sourceResult);
        }

        /**
         * hkeys
         * @param key
         * @return
         */
        @Override
        public String hkeys(String key) {
            List<String> sourceResult = new ArrayList<>(getExecuteClient().hKeys(key));
            return CommonCollectionUtils.list2String(sourceResult);
        }

        /**
         * hvals
         * @param key
         * @return
         */
        @Override
        public String hvals(String key) {
            List<String> sourceResult = getExecuteClient().hVals(key);
            return CommonCollectionUtils.list2String(sourceResult);
        }

        /**
         * hgetAll
         * @param key
         * @return
         */
        @Override
        public String hgetAll(String key) {
            Map<String, String> sourceResult = getExecuteClient().hGetAll(key);
            return CommonCollectionUtils.map2String(sourceResult);
        }

        /**
         * hscanMatchCount
         * @param key
         * @param cursorStr
         * @param params
         * @return
         */
        @Override
        public String hscan(String key, String cursorStr, Map<String, String> params) {
            ByteString cursor = ByteString.copyFromUtf8(cursorStr);

            ScanOptions.ScanOptionsBuilder scanOptions = ScanOptions.scanOptions();
            if (params.containsKey(CommonConstant.MATCH)) {
                scanOptions.match(params.get(CommonConstant.MATCH));
            }
            if (params.containsKey(CommonConstant.COUNT)) {
                scanOptions.count(Long.valueOf(params.get(CommonConstant.COUNT)));
            }

            ScanResult<Map.Entry<String, String>> sourceResult = getExecuteClient()
                    .hScan(key, cursor, scanOptions.build());

            return CommonCollectionUtils.scanResult2String(sourceResult);
        }
    }

    /**
     * HyperLogLogRedisService
     */
    private class HyperLogLogJimkvSdkServiceImpl implements HyperLogLogRedisService {

        /**
         * pfadd
         * @parma key
         * @param element
         * @return
         */
        @Override
        public String pfadd(String key, String... element) {
            Long sourceResult = getExecuteClient().pfAdd(key, element);
            return sourceResult == null ? CommonConstant.ZERO : sourceResult.toString();
        }

        /**
         * pfcount
         * @parma key
         * @return
         */
        @Override
        public String pfcount(String key) {
            Long sourceResult = getExecuteClient().pfCount(key);
            return sourceResult == null ? CommonConstant.ZERO : sourceResult.toString();
        }

        /**
         * TODO 暂时不支持此方法
         * pfmerge
         * @param destkey
         * @param sourcekey
         * @return
         */
        @Override
        public String pfmerge(String destkey, String... sourcekey) {
            throw new UnsupportedOperationException(String.format(CommonConstant.UN_SUPPORT_PREFIX, "pfMerge"));
        }

    }

    /**
     * InnerOrderRedisService
     */
    private class InnerOrderJimkvSdkServiceImpl implements InnerOrderRedisService {

        @Override
        public String dump(String key) {
            byte[] result = getExecuteClient().dump(key);
            return null == result ? CommonConstant.EMPTY : new String(result);
        }

        @Override
        public String restore(String key, long ttl, byte[] serializedValue) {
            return getExecuteClient().restore(key, serializedValue, ttl, TimeUnit.MILLISECONDS);
        }
    }

    /**
     * ListRedisService
     */
    private class ListJimkvSdkServiceImpl implements ListRedisService {

        @Override
        public String lPush(String key, String... values) {
            Long result = getExecuteClient().lPush(key, values);
            return null == result ? CommonConstant.ZERO : result.toString();
        }

        @Override
        public String lPop(String key) {
            return getExecuteClient().lPop(key);
        }

        @Override
        public String lPushX(String key, String value) {
            Long result = getExecuteClient().lPushX(key, value);
            return null == result ? CommonConstant.ZERO : result.toString();
        }

        @Override
        public String rPush(String key, String... values) {
            Long result = getExecuteClient().rPush(key, values);
            return null == result ? CommonConstant.ZERO : result.toString();
        }

        @Override
        public String rPushX(String key, String value) {
            Long result = getExecuteClient().rPushX(key, value);
            return null == result ? CommonConstant.ZERO : result.toString();
        }

        @Override
        public String rPop(String key) {
            return getExecuteClient().rPop(key);
        }

        @Override
        public String rPopLPush(String source, String destination) {
            return getExecuteClient().rPopLPush(source, destination);
        }

        @Override
        public String lRem(String key, long count, String value) {
            Long result = getExecuteClient().lRem(key, count, value);
            return null == result ? CommonConstant.ZERO : result.toString();
        }

        @Override
        public String lLen(String key) {
            Long result = getExecuteClient().lLen(key);
            return null == result ? CommonConstant.ZERO : result.toString();
        }

        @Override
        public String lIndex(String key, long index) {
            return getExecuteClient().lIndex(key, index);
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
            Position position1 = Position.valueOf(position);

            Long sourceResult = getExecuteClient().lInsert(key, position1, pivot, value);
            return sourceResult == null ? CommonConstant.ZERO : sourceResult.toString();
        }

        @Override
        public String lSet(String key, long index, String value) {
            getExecuteClient().lSet(key, index, value);
            return CommonConstant.OK;
        }

        @Override
        public String lRange(String key, long begin, long end) {
            return CommonCollectionUtils.list2String(getExecuteClient().lRange(key, begin, end));
        }

        @Override
        public String lTrim(String key, long begin, long end) {
            getExecuteClient().lTrim(key, begin, end);
            return CommonConstant.OK;
        }
    }

    /**
     * LuaRedisService
     */
    private class LuaJimkvSdkServiceImpl implements LuaRedisService {

        @Override
        public String eval(String script, List<String> keys, List<String> args) {
            throw new UnsupportedOperationException(String.format(CommonConstant.UN_SUPPORT_PREFIX, "eval"));
        }

        @Override
        public String evalsha(String sha, List<String> keys, List<String> args) throws ScriptNotFoundException {
            boolean readOnly = true;
            ScriptOutputType type = ScriptOutputType.VALUE;

            Object object = getExecuteClient().evalsha(sha, keys, args, readOnly, type);
            return null == object ? CommonConstant.EMPTY : object.toString();
        }
    }

    /**
     * SetRedisService
     */
    private class SetJimkvSdkServiceImpl implements SetRedisService {

        @Override
        public String sAdd(String key, String... values) {
            Long result = getExecuteClient().sAdd(key, values);
            return null == result ? CommonConstant.ZERO : result.toString();
        }

        @Override
        public String sIsMember(String key, String value) {
            Boolean result = getExecuteClient().sIsMember(key, value);
            return null == result ? CommonConstant.FALSE : result.toString();
        }

        @Override
        public String sPop(String key) {
            return getExecuteClient().sPop(key);
        }

        @Override
        public String sRandMember(String key, Long count) {
            return null == count ? getExecuteClient().sRandMember(key)
                    : CommonCollectionUtils.list2String(getExecuteClient().sRandMember(key, count));
        }

        @Override
        public String sRem(String key, String... values) {
            Long result = getExecuteClient().sRem(key, values);
            return null == result ? CommonConstant.ZERO : result.toString();
        }

        @Override
        public String sMove(String source, String destination, String value) {
            Boolean result = getExecuteClient().sMove(source, destination, value);
            return null == result ? CommonConstant.FALSE : result.toString();
        }

        @Override
        public String sCard(String key) {
            Long result = getExecuteClient().sCard(key);
            return null == result ? CommonConstant.ZERO : result.toString();
        }

        @Override
        public String sMembers(String key) {
            return CommonCollectionUtils.set2String(getExecuteClient().sMembers(key));
        }

        @Override
        public String sscan(String key, String cursorStr, Map<String, String> params) {

            ByteString cursor = ByteString.copyFromUtf8(cursorStr);

            ScanOptions.ScanOptionsBuilder optionsBuilder = ScanOptions.scanOptions();

            if (params.containsKey(CommonConstant.MATCH)) {
                optionsBuilder.match(params.get(CommonConstant.MATCH));
            }

            if (params.containsKey(CommonConstant.COUNT)) {
                optionsBuilder.count(Integer.valueOf(params.get(CommonConstant.COUNT)));
            }

            ScanOptions scanOptions = optionsBuilder.build();

            ScanResult<String> scanResult = getExecuteClient().sScan(key, cursor, scanOptions);

            return CommonCollectionUtils.scanResult2String(scanResult);
        }

        @Override
        public String sInter(String... keys) {
            return CommonCollectionUtils.set2String(getExecuteClient().sInter(keys));
        }

        @Override
        public String sInterStore(String destination, String... keys) {
            Long result = getExecuteClient().sInterStore(destination, keys);
            return null == result ? CommonConstant.ZERO : result.toString();
        }

        @Override
        public String sUnion(String... keys) {
            return CommonCollectionUtils.set2String(getExecuteClient().sUnion(keys));
        }

        @Override
        public String sUnionStore(String destination, String... keys) {
            Long result = getExecuteClient().sUnionStore(destination, keys);
            return null == result ? CommonConstant.ZERO : result.toString();
        }

        @Override
        public String sDiff(String... keys) {
            return CommonCollectionUtils.set2String(getExecuteClient().sDiff(keys));
        }

        @Override
        public String sDiffStore(String destination, String... keys) {
            Long result = getExecuteClient().sDiffStore(destination, keys);
            return null == result ? CommonConstant.ZERO : result.toString();
        }
    }

    /**
     * SortedSetRedisService
     */
    private class SortedSetJimkvSdkServiceImpl implements SortedSetRedisService {

        /**
         * zadd
         * @parma key
         * @param score
         * @param member
         */
        @Override
        public String zadd(String key, double score, String member) {
            Boolean sourceResult = getExecuteClient().zAdd(key, score, member);
            return sourceResult == null ? CommonConstant.FALSE: sourceResult.toString();
        }

        /**
         * zscore
         * @param key
         * @param member
         * @return
         */
        @Override
        public String zscore(String key, String member) {
            Double sourceResult = getExecuteClient().zScore(key, member);
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
            Double sourceResult = getExecuteClient().zIncrBy(key, delta, member);
            return sourceResult == null ? CommonConstant.ZERO : sourceResult.toString();
        }

        /**
         * zcard
         * @param key
         * @return
         */
        @Override
        public String zcard(String key) {
            Long sourceResult = getExecuteClient().zCard(key);
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
            Long sourceResult = getExecuteClient().zCount(key, min, max);
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
            Set<String> sourceResult = getExecuteClient().zRange(key, start, stop);
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
            Set<String> sourceResult = getExecuteClient().zRevRange(key, start, stop);
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
            Set<String> sourceResult = getExecuteClient().zRangeByScore(key, min, max);
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
            throw new UnsupportedOperationException(String.format(CommonConstant.UN_SUPPORT_PREFIX, "zrangeByScore(String key, String min, String max)"));
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
            Set<String> sourceResult = getExecuteClient().zRevRangeByScore(key, min, max);
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
            throw new UnsupportedOperationException(String.format(CommonConstant.UN_SUPPORT_PREFIX, "zrevrangeByScore(String key, String min, String max)"));
        }

        /**
         * zrank
         * @param key
         * @param member
         * @return
         */
        @Override
        public String zrank(String key, String member) {
            Long sourceResult = getExecuteClient().zRank(key, member);
            return sourceResult == null ? CommonConstant.ZERO : sourceResult.toString();
        }

        /**
         * zrevrank
         * @param key
         * @param member
         * @return
         */
        @Override
        public String zrevrank(String key, String member) {
            Long sourceResult = getExecuteClient().zRevRank(key, member);
            return sourceResult == null ? CommonConstant.ZERO : sourceResult.toString();
        }

        /**
         * zrem
         * @param key
         * @param member
         * @return
         */
        @Override
        public String zrem(String key, String... member) {
            Long sourceResult = getExecuteClient().zRem(key, member);
            return sourceResult == null ? CommonConstant.ZERO : sourceResult.toString();
        }

        /**
         * TODO
         * zremrangeByRank
         * @param key
         * @param start
         * @param stop
         * @return
         */
        @Override
        public String zremrangeByRank(String key, long start, long stop) {
            Long sourceResult = getExecuteClient().zRemRange(key, start, stop);
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
            Long sourceResult = getExecuteClient().zRemRangeByScore(key, min, max);
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
            throw new UnsupportedOperationException(String.format(CommonConstant.UN_SUPPORT_PREFIX, "zremrangeByScore(String key, String min, String max)"));
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
            Set<String> sourceResult = getExecuteClient().zRangeByLex(key, min, max);
            return CommonCollectionUtils.set2String(sourceResult);
        }

        /**
         * jimkvSDK 目前不支持该方法
         * @param key
         * @param min
         * @param max
         * @return
         */
        @Override
        public String zlexcount(String key, String min, String max) {
            throw new UnsupportedOperationException(String.format(CommonConstant.UN_SUPPORT_PREFIX, "zLexCount"));
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
            Long sourceResult = getExecuteClient().zRemRangeByLex(key, min, max);
            return sourceResult == null ? CommonConstant.ZERO : sourceResult.toString();
        }

        /**
         * zscan
         * @param key
         * @param cursorStr
         * @param params
         * @return
         */
        @Override
        public String zscan(String key, String cursorStr, Map<String, String> params) {
            ByteString cursor = ByteString.copyFromUtf8(cursorStr);

            ScanOptions.ScanOptionsBuilder scanOptionsBuilder = ScanOptions.scanOptions();
            if (params.containsKey(CommonConstant.MATCH)) {
                scanOptionsBuilder.match(params.get(CommonConstant.MATCH));
            }
            if (params.containsKey(CommonConstant.COUNT)) {
                scanOptionsBuilder.count(Long.valueOf(params.get(CommonConstant.COUNT)));
            }
            ScanOptions scanOptions = scanOptionsBuilder.build();

            ScanResult<ZSetTuple<String>> sourceResult =
                    getExecuteClient().zScan(key, cursor, scanOptions);

            return scanResultToString(sourceResult);
        }

        private String scanResultToString(ScanResult<ZSetTuple<String>> scanResult) {
            StringBuffer temp = new StringBuffer();
            temp.append(scanResult.getCursor().toString());
            List<ZSetTuple<String>> resultList = scanResult.getResult();
            if (resultList != null) {
                resultList.forEach(tuple -> {
                    temp.append(tuple.getScore());
                    temp.append(":");
                    temp.append(tuple.getValue());
                });
            }

            return temp.toString();
        }

        /**
         * zunionstore
         * @param destination
         * @param sets
         * @return
         */
        @Override
        public String zunionstore(String destination, String... sets) {
            Long sourceResult = getExecuteClient().zUnionStore(destination, sets);
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
            Long sourceResult = getExecuteClient().zInterStore(destination, sets);
            return sourceResult == null ? CommonConstant.ZERO : sourceResult.toString();
        }
    }

    /**
     * StringRedisService
     */
    private class StringJimkvSdkServiceImpl implements StringRedisService {

        @Override
        public String set(String key, String value) {
            getExecuteClient().set(key, value);
            return CommonConstant.OK;
        }

        @Override
        public String get(String key) {
            return getExecuteClient().get(key);
        }

        @Override
        public String setNX(String key, String value) {
            Boolean sourceResult = getExecuteClient().setNX(key, value);
            return null == sourceResult ? "false" : sourceResult.toString();
        }

        @Override
        public String setEx(String key, String value, long timeout, TimeUnit unit) {
            getExecuteClient().setEx(key, value, timeout, unit);
            return CommonConstant.OK;
        }

        @Override
        public String strLen(String key) {
            Long sourceResult = getExecuteClient().strLen(key);
            return null == sourceResult ? "0" : sourceResult.toString();
        }

        @Override
        public String setRange(String key, String value, long offset) {
            Long sourceResult = getExecuteClient().setRange(key, value, offset);
            return null == sourceResult ? "0" : sourceResult.toString();
        }

        @Override
        public String psetex(String key, long milliseconds, String value) {
            getExecuteClient().pSetEx(key, value, milliseconds, TimeUnit.MILLISECONDS);
            return CommonConstant.OK;
        }

        @Override
        public String mset(List<String> paramsList) {
            Map<String, String> tuple = Maps.newHashMap();

            for (int i = 0; i < paramsList.size()-1; i = i + 2) {
                tuple.put(paramsList.get(i), paramsList.get(i + 1));
            }

            getExecuteClient().mSetString(tuple);
            return CommonConstant.OK;
        }

        @Override
        public String mget(String... keys) {
            List<String> values = getExecuteClient().mGet(keys);

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
            return getExecuteClient().getRange(key, start, end);
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
            Double itemResult = getExecuteClient().incrBy(key, increment);
            return itemResult == null ? CommonConstant.ZERO : itemResult.toString();
        }

        @Override
        public String decr(String key) {
            Long itemResult = getExecuteClient().decr(key);
            return itemResult == null ? CommonConstant.ZERO : itemResult.toString();
        }

        @Override
        public String msetnx(List<String> paramsList) {
            throw new UnsupportedOperationException(String.format(CommonConstant.UN_SUPPORT_PREFIX, "msetnx"));
        }
    }

    /**
     * TransactionRedisService
     */
    private class TransactionJimkvSdkServiceImpl implements TransactionRedisService {

        @Override
        public String multi() {
            throw new UnsupportedOperationException(String.format(CommonConstant.UN_SUPPORT_PREFIX, "multi"));
        }
    }
}

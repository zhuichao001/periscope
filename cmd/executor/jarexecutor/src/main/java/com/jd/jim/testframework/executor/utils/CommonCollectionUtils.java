package com.jd.jim.testframework.executor.utils;

import com.jd.jim.testframework.executor.constant.CommonConstant;
import org.apache.commons.collections4.CollectionUtils;
import redis.clients.jedis.ScanResult;

import java.util.*;

/**
 * Description:
 * Author: wangjinshuai
 * Date: 2020-12-23 14:07
 * Email: wangjinshuai@jd.com
 */
public class CommonCollectionUtils {

    /**
     * list to string
     * @param list
     * @return
     */
    public static String list2String(List<String> list) {
        if (CollectionUtils.isEmpty(list)) {
            return CommonConstant.EMPTY;
        }

        return Arrays.toString(list.stream().toArray());
    }

    /**
     * set to string
     * @param set
     * @return
     */
    public static String set2String(Set<String> set) {
        if (CollectionUtils.isEmpty(set)) {
            return CommonConstant.EMPTY;
        }

        List<String> list = new ArrayList<>(set);
        Collections.sort(list);

        return list2String(list);
    }

    /**
     * map to string
     * @param map
     * @return
     */
    public static String map2String(Map<String, String> map) {
        if (map == null || map.isEmpty()) {
            return CommonConstant.EMPTY;
        }

        return CommonConstant.MAP_JOINER.join(new TreeMap<>(map));
    }

    /**
     * ScanResult to string
     * @param scanResult
     * @return
     */
    public static String scanResult2String(ScanResult scanResult) {
        if (CollectionUtils.isEmpty(scanResult.getResult())) {
            return CommonConstant.EMPTY;
        }

        return list2String(scanResult.getResult());
    }

    /**
     * ScanResult to string
     * @param scanResult
     * @return
     */
    public static String scanResult2String(com.jd.jim.cli.protocol.ScanResult scanResult) {
        if (CollectionUtils.isEmpty(scanResult.getResult())) {
            return CommonConstant.EMPTY;
        }

        return list2String(scanResult.getResult());
    }

    /**
     * ScanResult to string
     * @param scanResult
     * @return
     */
    public static String scanResult2String(com.jd.jim.cli.protocol.KeyScanResult scanResult) {
        if (CollectionUtils.isEmpty(scanResult.getResult())) {
            return CommonConstant.EMPTY;
        }

        return list2String(scanResult.getResult());
    }

}

package com.jd.jim.testframework.executor.handle.zset;

import com.alibaba.fastjson.JSON;
import com.jd.jim.testframework.executor.constant.CommonConstant;
import com.jd.jim.testframework.executor.exception.InvalidParamException;
import com.jd.jim.testframework.executor.handle.BaseHandler;
import lombok.extern.slf4j.Slf4j;
import org.apache.commons.collections4.CollectionUtils;
import org.springframework.stereotype.Service;

import java.util.List;

@Slf4j
@Service(value = "zUnionStoreHandler")
public class ZUnionStoreHandler extends BaseHandler {

    @Override
    public String handle(List<String> commandList) {

        if (CollectionUtils.isEmpty(commandList) || commandList.size() < 2) {
            throw new InvalidParamException(CommonConstant.INVALID_PARAM);
        }

        String destination = commandList.get(0);

        int numKeys = Integer.valueOf(commandList.get(1));

        int start = 2;

        int end = start + numKeys;

        if (end > commandList.size()) {
            log.error("ZUnionStoreHandler invalid params, commandList:{}", JSON.toJSONString(commandList));
            throw new InvalidParamException(CommonConstant.INVALID_PARAM);
        }

        String[] keys = commandList.subList(2, 2 + numKeys).toArray(new String[0]);

        return redisService.getSortedSetRedisService().zunionstore(destination, keys);
    }

}

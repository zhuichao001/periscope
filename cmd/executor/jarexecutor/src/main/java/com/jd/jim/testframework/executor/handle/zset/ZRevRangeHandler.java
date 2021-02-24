package com.jd.jim.testframework.executor.handle.zset;

import com.jd.jim.testframework.executor.constant.CommonConstant;
import com.jd.jim.testframework.executor.exception.InvalidParamException;
import com.jd.jim.testframework.executor.handle.BaseHandler;
import lombok.extern.slf4j.Slf4j;
import org.apache.commons.collections4.CollectionUtils;
import org.springframework.stereotype.Service;

import java.util.List;

@Slf4j
@Service(value = "zRevRangeHandler")
public class ZRevRangeHandler extends BaseHandler {

    @Override
    public String handle(List<String> commandList) {
        if (CollectionUtils.isEmpty(commandList) || commandList.size() < 3) {
            throw new InvalidParamException(CommonConstant.INVALID_PARAM);
        }

        String key = commandList.get(0);
        long min = Long.valueOf(commandList.get(1));
        long max = Long.valueOf(commandList.get(2));

        return redisService.getSortedSetRedisService().zrevrange(key, min, max);
    }

}

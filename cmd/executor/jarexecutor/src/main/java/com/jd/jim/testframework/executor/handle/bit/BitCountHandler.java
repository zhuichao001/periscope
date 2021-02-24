package com.jd.jim.testframework.executor.handle.bit;

import com.jd.jim.testframework.executor.handle.BaseHandler;
import lombok.extern.slf4j.Slf4j;
import org.apache.commons.collections4.CollectionUtils;
import org.springframework.stereotype.Service;

import java.util.List;

@Slf4j
@Service(value = "bitCountHandler")
public class BitCountHandler extends BaseHandler {

    @Override
    public String handle(List<String> commandList) {

        String key = commandList.get(0);

        if (!CollectionUtils.isEmpty(commandList) && commandList.size() >= 3) {
            long start = Long.valueOf(commandList.get(1));
            long end = Long.valueOf(commandList.get(2));
            return redisService.getBitRedisService().bitcount(key, start, end);
        } else {
            return redisService.getBitRedisService().bitcount(key);
        }
    }
}

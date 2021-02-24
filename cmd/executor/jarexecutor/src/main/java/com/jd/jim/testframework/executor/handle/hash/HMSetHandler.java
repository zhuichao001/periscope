package com.jd.jim.testframework.executor.handle.hash;

import com.jd.jim.testframework.executor.constant.CommonConstant;
import com.jd.jim.testframework.executor.exception.InvalidParamException;
import com.jd.jim.testframework.executor.handle.BaseHandler;
import lombok.extern.slf4j.Slf4j;
import org.apache.commons.collections4.CollectionUtils;
import org.springframework.stereotype.Service;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

@Slf4j
@Service(value = "hMSetHandler")
public class HMSetHandler extends BaseHandler {

    @Override
    public String handle(List<String> commandList) {

        if (CollectionUtils.isEmpty(commandList) || commandList.size() < 3) {
            throw new InvalidParamException(CommonConstant.INVALID_PARAM);
        }

        String key = commandList.get(0);
        Map<String, String> hash = new HashMap<>();
        for (int i=1; i<commandList.size(); i+=2) {
            if (i+1 < commandList.size()) {
                hash.put(commandList.get(i), commandList.get(i+1));
            }
        }

        return redisService.getHashRedisService().hmset(key, hash);
    }
}

package com.jd.jim.testframework.executor.handle.hash;

import com.jd.jim.testframework.executor.constant.CommonConstant;
import com.jd.jim.testframework.executor.exception.InvalidParamException;
import com.jd.jim.testframework.executor.handle.BaseHandler;
import lombok.extern.slf4j.Slf4j;
import org.apache.commons.collections4.CollectionUtils;
import org.springframework.stereotype.Service;

import java.util.List;

@Slf4j
@Service(value = "hIncrByFloatHandler")
public class HIncrByFloatHandler extends BaseHandler {

    @Override
    public String handle(List<String> commandList) {

        if (CollectionUtils.isEmpty(commandList) || commandList.size() < 3) {
            throw new InvalidParamException(CommonConstant.INVALID_PARAM);
        }

        String key = commandList.get(0);
        String field = commandList.get(1);
        double delta = Double.parseDouble(commandList.get(2));

        return redisService.getHashRedisService().hincrByFloat(key, field, delta);
    }
}

package com.jd.jim.testframework.executor.handle.list;

import com.jd.jim.testframework.executor.constant.CommonConstant;
import com.jd.jim.testframework.executor.exception.InvalidParamException;
import com.jd.jim.testframework.executor.handle.BaseHandler;
import lombok.extern.slf4j.Slf4j;
import org.apache.commons.collections4.CollectionUtils;
import org.springframework.stereotype.Service;

import java.util.List;

@Slf4j
@Service(value = "linsertHandler")
public class LinsertHandler extends BaseHandler {

    @Override
    public String handle(List<String> commandList) {

        if (CollectionUtils.isEmpty(commandList) || commandList.size() < 4) {
            throw new InvalidParamException(CommonConstant.INVALID_PARAM);
        }

        String key = commandList.get(0);
        String position = commandList.get(1);
        String pivot = commandList.get(2);
        String value = commandList.get(3);

        return redisService.getListRedisService().lInsert(key, position, pivot, value);
    }
}

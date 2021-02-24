package com.jd.jim.testframework.executor.handle.db;

import com.jd.jim.testframework.executor.constant.CommonConstant;
import com.jd.jim.testframework.executor.exception.InvalidParamException;
import com.jd.jim.testframework.executor.handle.BaseHandler;
import lombok.extern.slf4j.Slf4j;
import org.apache.commons.collections4.CollectionUtils;
import org.springframework.stereotype.Service;

import java.util.List;

@Slf4j
@Service(value = "moveHandler")
public class MoveHandler extends BaseHandler {

    @Override
    public String handle(List<String> commandList) {
        if (CollectionUtils.isEmpty(commandList) || commandList.size() < 2) {
            throw new InvalidParamException(CommonConstant.INVALID_PARAM);
        }

        String key = commandList.get(0);
        int index = Integer.getInteger(commandList.get(1));

        return redisService.getDbRedisService().move(key, index);
    }
}

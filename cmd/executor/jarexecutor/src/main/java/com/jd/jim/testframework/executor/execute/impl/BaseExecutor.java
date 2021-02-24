package com.jd.jim.testframework.executor.execute.impl;

import com.jd.jim.testframework.executor.domain.CommandInfo;
import com.jd.jim.testframework.executor.factory.CommonBeanFactory;
import com.jd.jim.testframework.executor.handle.BaseHandler;
import com.jd.jim.testframework.executor.redis.RedisService;
import lombok.extern.slf4j.Slf4j;
import org.apache.commons.lang3.StringUtils;

@Slf4j
public abstract class BaseExecutor extends AbstractExecutor {

    public abstract RedisService getRedisService();

    @Override
    public String executeCommand(CommandInfo commandInfo) throws Exception {
        String handlerClassName = commandInfo.getCommandEnum().getHandlerClassName();

        if (StringUtils.isEmpty(handlerClassName)) {
            log.error("Executor handlerClassName empty commandInfo:{}", commandInfo);
            throw new UnsupportedOperationException(commandInfo.getCommand());
        } else {
            BaseHandler baseHandler = CommonBeanFactory.getBean(handlerClassName, BaseHandler.class);
            baseHandler.setRedisService(getRedisService());
            return baseHandler.handle(commandInfo.getDetailList());
        }
    }

}
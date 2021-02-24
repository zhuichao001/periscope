package com.jd.jim.testframework.executor.handle.transaction;

import com.jd.jim.testframework.executor.handle.BaseHandler;
import org.springframework.stereotype.Service;

import java.util.List;

/**
 * Description:
 * Author: wangjinshuai
 * Date: 2020-12-15 15:52
 * Email: wangjinshuai@jd.com
 */
@Service
public class MultiHandler extends BaseHandler {

    @Override
    public String handle(List<String> commandList) {

        return redisService.getTransactionRedisService().multi();
    }
}

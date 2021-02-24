package com.jd.jim.testframework.executor.handle.db;

import com.jd.jim.testframework.executor.handle.BaseHandler;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;

import java.util.List;

@Slf4j
@Service(value = "dbSizeHandler")
public class DBSizeHandler extends BaseHandler {

    @Override
    public String handle(List<String> commandList) {
        return redisService.getDbRedisService().dbSize();
    }
}

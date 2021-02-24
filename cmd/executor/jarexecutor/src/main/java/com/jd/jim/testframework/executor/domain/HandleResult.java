package com.jd.jim.testframework.executor.domain;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

/**
 * Description:
 * Author: wangjinshuai
 * Date: 2020-12-15 15:12
 * Email: wangjinshuai@jd.com
 */
@NoArgsConstructor
@AllArgsConstructor
@Data
public class HandleResult {

    /**
     * 源集群结果
     */
    private String source;

    /**
     * 目标集群结果
     */
    private String dest;
}

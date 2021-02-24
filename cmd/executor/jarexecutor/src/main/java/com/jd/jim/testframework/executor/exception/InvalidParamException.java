package com.jd.jim.testframework.executor.exception;

/**
 * Description:
 * Author: wangjinshuai
 * Date: 2020-12-28 14:14
 * Email: wangjinshuai@jd.com
 */
public class InvalidParamException extends RuntimeException {

    public InvalidParamException() {
        super();
    }

    public InvalidParamException(String message) {
        super(message);
    }

    public InvalidParamException(String message, Throwable cause) {
        super(message, cause);
    }
}

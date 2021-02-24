package com.jd.jim.testframework.executor.factory;

import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.BeansException;
import org.springframework.context.ApplicationContext;
import org.springframework.context.ApplicationContextAware;
import org.springframework.stereotype.Component;

/**
 * Description:
 * User: wangjinshuai
 * Time: 2019-01-22 10:04
 * Email: wangjinshuai@jd.com
 */
@Component
@Slf4j
public class CommonBeanFactory implements ApplicationContextAware {

    private static ApplicationContext context;

    @Override
    public void setApplicationContext(ApplicationContext applicationContext) throws BeansException {
        CommonBeanFactory.context = applicationContext;
    }

    public static ApplicationContext getContext() {
        return context;
    }

    /**
     * 通过 beanName 获取 bean
     * @param beanName
     * @param clazz
     * @param <T>
     * @return
     */
    public static <T> T getBean(String beanName, Class<T> clazz) {
        return getContext().getBean(beanName, clazz);
    }

    /**
     * 通过 类型 获取 bean
     * @param clazz
     * @param <T>
     * @return
     */
    public static <T> T getBean(Class<T> clazz) {
        return getContext().getBean(clazz);
    }
}

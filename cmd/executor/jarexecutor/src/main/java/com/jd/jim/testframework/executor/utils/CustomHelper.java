package com.jd.jim.testframework.executor.utils;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class CustomHelper {

    public static Map<String, String> commandList2Map(List<String> commandList) {
        Map<String, String> params = new HashMap<>();

        for (int i=0; i<commandList.size()-1; i+=2) {
            params.put(commandList.get(i).toUpperCase(), commandList.get(i+1));
        }

        return params;
    }
}

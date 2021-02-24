package com.jd.jim.testframework.executor.utils;

import org.junit.Assert;
import org.junit.Test;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class CommonCollectionUtilsTest {

    @Test
    public void testList2String() {
        List<String> list1 = new ArrayList<>();
        list1.add("a");
        list1.add("b");
        list1.add("c");
        Assert.assertEquals("[a, b, c]", CommonCollectionUtils.list2String(list1));

        List<String> list2 = new ArrayList<>();
        list2.add("a");
        list2.add("b");
        list2.add(null);
        Assert.assertEquals("[a, b, null]", CommonCollectionUtils.list2String(list2));

        List<String> list3 = new ArrayList<>();
        list3.add("a");
        list3.add("b");
        list3.add("");
        Assert.assertEquals("[a, b, ]", CommonCollectionUtils.list2String(list3));
    }

    @Test
    public void testSet2String() {
        Set<String> set1 = new HashSet<>();
        set1.add("c");
        set1.add("a");
        set1.add("b");
        Assert.assertEquals("[a, b, c]", CommonCollectionUtils.set2String(set1));

        Set<String> set2 = new HashSet<>();
        set2.add("a");
        set2.add("b");
        set2.add("a");
        Assert.assertEquals("[a, b]", CommonCollectionUtils.set2String(set2));
    }
}

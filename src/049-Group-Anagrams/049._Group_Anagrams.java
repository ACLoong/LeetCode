package leetcode;

import java.util.*;

public class GroupAnagrams_049 {
    public static  List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> res = new ArrayList<>();
        if(strs == null || strs.length == 0){
            return res;
        }
        Map<String,List<String>> map = new HashMap<>();
        for(String str : strs){
            List<String> list = new ArrayList<>();
            list.add(str);
            char[] chars = str.toCharArray();
            Arrays.sort(chars);
            if(map.containsKey(String.valueOf(chars))){
                map.get(String.valueOf(chars)).add(str);
            }else{
                map.put(String.valueOf(chars),list);
            }
        }
        for(Map.Entry<String,List<String>> entry : map.entrySet()){
            res.add(entry.getValue());
        }
        return res;
    }
}

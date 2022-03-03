package KillProcess;

import java.util.*;

public class KillProcess {
    public static void main(String[] args) {
        List<Integer> pidList = new ArrayList();
        pidList.add(1);
        pidList.add(3);
        pidList.add(10);
        pidList.add(5);

        List<Integer> ppidList = new ArrayList();
        ppidList.add(3);
        ppidList.add(0);
        ppidList.add(5);
        ppidList.add(3);

        System.out.println("resutl: " + killProcess(pidList, ppidList, 5));
    }

    public static List<Integer> killProcess(List<Integer> pid, List<Integer> ppid, int kill) {
        Map<Integer, Set<Integer>> parentChildMap = new HashMap();
        Iterator parentIt = ppid.iterator();
        int j = 0;
        while(parentIt.hasNext()) {
            int parentId = (int)parentIt.next();
            if(!parentChildMap.containsKey(parentId)) {
                parentChildMap.put(parentId, new HashSet());
            }
            parentChildMap.get(parentId).add(j);
            j++;
        }
//        System.out.println(parentChildMap);
        List<Integer> killList = new ArrayList();
        killProcHelper(pid, parentChildMap, kill, killList);
        return killList;
    }

    public static void killProcHelper(List<Integer> pid, Map<Integer, Set<Integer>> parentChildMap, int kill, List<Integer> killList) {
        killList.add(kill);
        if(!parentChildMap.containsKey(kill)) {
            return;
        }
        for(int child :parentChildMap.get(kill)) {
            killProcHelper(pid, parentChildMap, (int)pid.get(child), killList);
        }
    }

    public static List<Integer> killProcess2(List<Integer> pid, List<Integer> ppid, int kill) {
        Map<Integer, List<Integer>> children = new HashMap();

        for(int i=0; i<pid.size(); i++){
            Integer parent = ppid.get(i);
            children.putIfAbsent(parent, new ArrayList());
            children.get(parent).add(pid.get(i));
        }

        List<Integer> ans = new ArrayList();
        Queue<Integer> q = new LinkedList();
        q.add(kill);

        while(!q.isEmpty()){
            Integer current = q.poll();
            ans.add(current);
            q.addAll(children.getOrDefault(current,new LinkedList()));
        }

        return ans;
    }
}

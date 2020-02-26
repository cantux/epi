    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        seen = set()
        len_r = len(rooms)
        
        q = deque([0])
        while q:
            curr = q.popleft()
            seen.add(curr)
            for n in rooms[curr]:
                if n not in seen:
                    q.append(n)

        return len(seen) == len_r

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        count_map = collections.defaultdict(int)
        for cpdomain in cpdomains:
            count, domain = cpdomain.split()
            count = int(count)
            count_map[domain] += count
            for index in range(len(domain)):
                if domain[index] == '.':
                    count_map[domain[index + 1:]] += count
        result = []
        for domain in count_map.keys():
            result.append(str(count_map[domain]) + ' ' + domain)
        return result
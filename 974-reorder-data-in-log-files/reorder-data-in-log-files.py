class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        n = len(logs)
        digit_logs = [log for log in logs if log.split()[1].isdigit()]
        letter_logs = sorted([log for log in logs if log.split()[1].isalpha()], key=lambda x: (' '.join(x.split()[1:]), x.split()[0]))
        return letter_logs + digit_logs
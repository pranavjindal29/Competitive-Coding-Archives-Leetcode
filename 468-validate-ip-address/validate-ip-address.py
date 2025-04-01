class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def is_valid_ipv4(ip: str) -> bool:
            octets = ip.split(".")
            if len(octets) != 4:
                return False
            for octet in octets:
                if not octet.isdigit() or str(int(octet)) != octet or int(octet) > 255:
                    return False
            return True

        def is_valid_ipv6(ip: str) -> bool:
            hextets = ip.split(":")
            if len(hextets) != 8:
                return False
            for hextet in hextets:
                if len(hextet) < 1 or len(hextet) > 4:
                    return False
                for char in hextet.lower():
                    if not ('a' <= char <= 'f' or '0' <= char <= '9'):
                        return False
            return True

        if is_valid_ipv4(queryIP):
            return "IPv4"
        return "IPv6" if is_valid_ipv6(queryIP) else "Neither"
        
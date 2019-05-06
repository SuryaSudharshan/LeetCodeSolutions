class Solution:
    def numUniqueEmails(self, emails) -> int:
        for email in emails:
            i = email.split("@")
            local = i[0].replace(".","")
            new_local = local.split("+")[0]
            new_email = new_local+ i[1]
            emails[emails.index(email)] = new_email
        return len(set(emails))
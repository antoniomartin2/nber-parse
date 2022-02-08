# nber-parse
Antonio Martin

The Parser reads NBER's Weekly Digest emails, tokenizes the descriptions of articles in the emails, and converts them to objects.

After parsing, the Util class has a method to determine if any of the articles are authored by Haas/IBSI affiliated researchers.

Plans exist to move this code into the cloud, so that emails can automatically analyzed upon receipt.

# Module 4 - Code Signing

**Goal**: Learn Sign a file

## Steps

1. Generate a GPG key pair

  ```bash
  gpg --full-generate-key
  ```

2. Follow the prompts. You may use any email, it doesn't need to be real. When asked for a passphrase, leave it empty and confirm

3. Export your keys:

```bash
gpg --export -a "email-address-you-used" > public.key
gpg --export-secret-keys -a "email-address-you-used" > private.key
```

4. Upload both files as a **project** secret on Semaphore

- Path: `/root/public.key`
- Path: `/root/private.key`

5. To import them in your CI job use:

  ```bash
  gpg --import /root/public.key
  gpg --import /root/private.key
  ```

6. To generate a signature for the artifact (remember to store the signature as an artifact):

  ```bash
  gpg --output artifact.txt.sig --detach-sign artifact.txt
  ```

7. To verify the signature, use the following command in a job.

  ```bash
  gpg --verify artifact.txt.sig artifact.txt
  ```

Make sure you have a job to sign and one to verify the signature

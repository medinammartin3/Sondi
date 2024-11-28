> [!NOTE]
> This is a personal project currently in development. It is expected to be released by February 2025.  
> You can see a demonstration video [here](#).

# Sondi: A Web Application for Online Polls

**Sondi** is a free and user-friendly platform for creating, sharing, and participating in online polls. Built with **Django**, Sondi empowers users to voice their opinions anonymously and make decisions collaboratively.

<br>

## Features

### What You Can Do
- **Create Polls**:  
  Easily create polls with multiple options, choosing between private and public visibility.

- **Vote Anonymously**:  
  Participate in polls without revealing your identity and see real-time results (with chart visualisation option).

- **Share Polls**:  
  Share your polls with friends, colleagues, or the world by providing a unique poll code.

- **Manage Your Polls**:  
  Keep track of all your polls in one place, view and analyze results, and close polls when they're finished.

- **Explore Public Polls**:  
  Find a pool of public questions to vote on in the **Public Polls** section, with options to sort them into different categories.

### Privacy at the Core
- **Your votes are anonymous**: Poll creators cannot see your name or identify voters.  
- **Accounts enhance functionality**: Required to manage your polls, prevent duplicate voting, and access your poll results.  
- **Private results**: Only poll creators can access the complete results. Public users see results immediately after voting, based on the data at that time.
- **Confidential Information Encryption**: All user-sensitive information, such as passwords, is encrypted and securely stored in the database. Sondi's administrators do not have access to raw confidential information, ensuring your data remains private and secure.

<br>

## Why Choose Sondi?
- **Simplicity**: User friendly and easy-to-use platform for everyone.  
- **Anonymity**: Ensures complete privacy for voters.  
- **Control**: Poll creators retain full control over their polls and results.  
- **Free Access**: No cost for creating or participating in polls.

<br>

## Technical Overview
- **Framework**: Developed with Django.  
- **Database**: Simple SQLite database for reliable storage.  
- **Admin Tools**: Django's built-in admin site for streamlined management.  
- **Concurrency Handling**: Robust mechanisms to prevent race conditions.  
- **Authentication**: Secure user authentification and accounts management.  
- **Unique Poll Codes**:  
  Polls are assigned unique codes using **Uid2**, a lightweight and highly efficient random code generator.  
  - **Prevent Collisions**: Ensures that every poll code is unique, even for a large number of polls.  
  - **Compact & Readable**: Generates short, user-friendly codes, making it easy to share and remember.  
  - **Performance**: Fast generation, even at scale, without impacting application performance.  
  - **Reliability**: Uid2's algorithm is robust, reducing the risk of duplication or errors.
- **Custom Admin Panel**:  
  Sondi's administrators have access to a custom admin site where they can manage users, polls, and everything needed to respond to any user needs effectively. This ensures the platform remains user-friendly and well-maintained.  
> [!IMPORTANT]
> **No Privacy Concerns**: Administrators do not have access to raw confidential user information. Sensitive data like passwords is encrypted and stored securely in the database, maintaining user privacy.

<br>

## Credits

This is a personal project currently in development.  
It is expected to be released by February 2025.

<br>

```txt
©  /\\/\//\//\
  \|/|\|/|\|/|/
 /|/|\|/|\|\’ .\
 ‘`|_|————|_|———o
```

# Solve It

Notes on problem solving, low level design, high level design.

## To do <!--todo:-->

- amortized time calculation in problem solving (refer cracking the code book)
- make your own markdown table for time and space complexity chart for different operations, algorithms, etc. [best, worst, avg, and special cases if any].
- problem solving - majority element --> Moore's voting algorithm.
- DSA notes repo --> Hashing.pdf (data structures based on hashing - unordered set, unordered map)
- DSA notes repo --> see everything (<https://github.com/Deeksha2501/Data-Structures-and-Algorithms-Notes>)

## Temporary Notes

- Reliability=The ability to work properly(even some parts/components failed).
- Durability=The ability of not losing data.
- Availability=The ability of less downtime, this rely on type of downtimes.

### Harry Potter problem in item based collaborative filtering algorithm in recommendation systems

- Let's say many users who watched Show A also watched Show B (e.g., both are popular). The recommendation system will pick up on this correlation and suggest Show B to anyone who watches Show A, regardless of whether that user might actually prefer niche or lesser-known shows. This happens because collaborative filtering relies on patterns of user behavior across large datasets.
- Here's how the problem manifests:
  - Show A (Harry Potter) is extremely popular and watched by a huge number of users.
  - Collaborative filtering algorithms detect that many users who watched Show A also watched Show B (another popular show).
  - As a result, if a new user watches Show A, the system is likely to recommend Show B, even though the user might prefer something less mainstream.
  - Over time, Show B gets recommended over and over again, reinforcing its popularity and making it harder for niche or less popular shows to be recommended.
- Thus, in collaborative filtering, popular shows (like Harry Potter) dominate recommendations because of their high overlap in user activity, even if a user might prefer a more unique or less popular option.

# The Plan
## Version 0.1
This is to just get something working to be able to focus more on the azure web-app side of the project.

The plan is as follows:

1. Create a random decorum setup from a set of aimiable setups. This will be our target solution.
2. Add 2 RoomsWith/NumComp conditions (one to each player)
    - RoomsWith must only:
        - Check AnyOf conditions
        - Be part of condition where 0.2 \< SSRF \< 0.8
        - Be part of condition with different target type to checked condition
3. Add 1 Non-forcing House condition (not NumComp) (to one player)
4. Add 1 weak forcing condition to bring to some mid-target SSRF (to other player). Current mid-target is 
5. Accumulate rest of conditions (non-forcing) to reach a desired multiplicative SSRF (ignorance lack of independence). Current target is 5e-13. Note that some conditions are built from multiple base conditions.

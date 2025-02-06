from typing import List


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        return self.tupleSameProductFrequencyMap(nums)

    # compute all products and create map of frequency of them
    # Go over frequency map and compute how many tuples there are
    # Time O(n^2), Space O(n2) 
    def tupleSameProductFrequencyMap(self, nums: List[int]) -> int:
        products_frequency = dict()

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                product = nums[i] * nums[j]

                if product in products_frequency:
                    products_frequency[product] += 1
                else:
                    products_frequency[product] = 1

        total_number_of_tuples = 0

        # Iterate through each product value and its frequency in the dictionary
        for product_frequency in products_frequency.values():
            # Calculate the number of ways to choose two pairs with the same product
            pairs_of_equal_product = (((product_frequency - 1) * product_frequency) // 2)

            # Add the number of tuples for this product to the total (each pair can form 8 tuples)
            total_number_of_tuples += 8 * pairs_of_equal_product

        return total_number_of_tuples


    # compute all products and create list of them
    # Sort list, if same product back to back then 8 pairs can make that
    # Time O(n^2logn), Space O(n2)
    def tupleSameProductFrequencyCount(self, nums: List[int]) -> int:
        products = []

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                products.append(nums[i] * nums[j])
        
        products.sort()

        total_number_of_tuples = 0
        last_product_seen = -1
        same_product_count = 0

        # Iterate over products to count how many times each product occurs
        for product_index in range(len(products)):
            if products[product_index] == last_product_seen:
                # Increment the count of same products
                same_product_count += 1
            else:
                # Calculate how many pairs had the previous product value
                pairs_of_equal_product = (((same_product_count - 1) * same_product_count) // 2)

                total_number_of_tuples += 8 * pairs_of_equal_product

                # Update last_product_seen and reset same_product_count
                last_product_seen = products[product_index]
                same_product_count = 1

        # Handle the last group of products (since the loop ends without adding it)
        pairs_of_equal_product = (((same_product_count - 1) * same_product_count) // 2)
        total_number_of_tuples += 8 * pairs_of_equal_product

        return total_number_of_tuples

    # Brute force implementation with some optimizations by creating hash map
    # Time O(n^3), Space O(n)
    def tupleSameProductLessBruteForce(self, nums: List[int]) -> int:
        # Sort the array for pruning purposes
        nums.sort()
        numsSet = set(nums)

        numTuples = 0
        # Iterate over list
        for i in range(len(nums)):
            # Find pair to create product and look for
            for j in range(len(nums)):
                if i == j:
                    continue

                targetProduct = nums[i] * nums[j]
                # Find pairs that create targetProduct
                for k in range(len(nums)):
                    # Make sure we aren't getting target with same pair as before
                    if k == i or k == j:
                        continue

                    # If we are already too large numbers will just keep getting larger, so break out of this loop
                    if nums[k] > targetProduct:
                        break
                    
                    # see if the current product is divisible by current num, if not skip
                    if targetProduct % nums[k] != 0:
                        continue

                    # See if the required pair is here and not the same number twice
                    if (targetProduct / nums[k]) in numsSet and (targetProduct / nums[k]) != nums[k]:
                        numTuples += 1

        return numTuples

    # Brute force implementation where you sort the list then iterate over all pairs
    # Time O(n^4), space O(1)
    def tupleSameProductBruteForce(self, nums: List[int]) -> int:
        # Sort the array for pruning purposes
        nums.sort()

        numTuples = 0
        # Iterate over list
        for i in range(len(nums)):
            # Find pair to create product and look for
            for j in range(len(nums)):
                if i == j:
                    continue

                targetProduct = nums[i] * nums[j]
                # Find pairs that create targetProduct
                for k in range(len(nums)):
                    # Make sure we aren't getting target with same pair as before
                    if k == i or k == j:
                        continue
                    for l in range(len(nums)):
                        # Make sure we aren't getting target with same pair as before
                        if l == i or l == j or l == k:
                            continue

                        testProduct = nums[k] * nums[l]
                        # if testProduct is the same as product we are looking for add tuple
                        # then break as the next number will be too large due to sorting
                        if testProduct == targetProduct:
                            numTuples += 1
                            break
                        # if testProduct is already larger than the target break as it won't get smaller
                        elif testProduct > targetProduct:
                            break

        return numTuples
    
testCases = [
    [[1,3,4,12], 8],
    [[2,3,4,6], 8],
    [[4,2,3,6], 8],
    [[1,2,4,5,10], 16],
    [[2,3,4,6,8,12], 40]
]
solution = Solution()
for nums, expected in testCases:
    answer = solution.tupleSameProduct(nums)
    if answer != expected:
        print(f"FAILED TEST: Expected {expected}, got {answer}. Input: {nums}")

print("Ran all test cases")
        int l2, r2, mid2, ans2;
        l2 = 0;
        r2 = nums.length - 1;
        ans2 = -100;

        while (l2 <= r2) {
            mid2 = l2 + (r2 - l2) / 2;
            if (nums[mid2] > target) {
                ans2 = mid2;
                r2 = mid2 - 1;
            } else {
                l2 = mid2 + 1;
            }
        }
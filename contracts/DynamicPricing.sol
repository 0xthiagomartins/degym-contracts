// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract DynamicPricing {
    uint public basePrice = 1 ether;

    function calculatePrice(
        uint timeOfDay,
        uint dayOfWeek,
        uint userCount
    ) external view returns (uint) {
        uint price = basePrice;

        // Adjust price based on time of day (e.g., peak hours)
        if (timeOfDay >= 6 && timeOfDay <= 9) {
            price += basePrice / 2; // 50% increase during morning peak
        } else if (timeOfDay >= 17 && timeOfDay <= 20) {
            price += basePrice / 2; // 50% increase during evening peak
        }

        // Adjust price based on day of the week (e.g., weekends)
        if (dayOfWeek == 6 || dayOfWeek == 0) {
            price += basePrice / 4; // 25% increase during weekends
        }

        // Adjust price based on current user count
        price += userCount * 1e16; // Increase price by 0.01 ether per user

        return price;
    }
}

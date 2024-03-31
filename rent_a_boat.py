def rent_a_boat() -> None:
    try:
        seasons: list[str] = ["Spring", "Summer", "Autumn", "Winter"]
        prices: dict[str, int] = {
            seasons[0]: 3000,
            seasons[1]: 4200,
            seasons[2]: 4200,
            seasons[3]: 2600,
        }

        budget = int(input("What is your budget? "))
        assert (
            budget >= 1 and budget <= 8000
        ), "Budget number must be between 1 and 8000!"

        group = int(input("How many people are in your group? "))
        assert group >= 4 and group <= 18, "Group number must be between 4 and 18!"

        season = int(
            input(
                f"""
            What season is it?
            1. {seasons[0]}
            2. {seasons[1]}
            3. {seasons[2]}
            4. {seasons[3]}
        """
            )
        )
        assert season > 0 and season < 5, "Season number must be between 1 and 4!"

        price: int = prices[seasons[season - 1]]

        match group:
            case group if group <= 6:
                price *= 0.9
            case group if group > 6 and group <= 11:
                price *= 0.85
            case group if group >= 12:
                price *= 0.75
            case _:
                price *= 1

        if group % 2 == 0 and season != 3:
            price *= 0.95

        assert (
            budget >= price
        ), f"You don't have enough money to rent a boat! You need {price - budget} USD more!"

        print(f"Yes! You have {budget - price} USD left.")
    except AssertionError as e:
        print(e)
        return

    except ValueError:
        print("Invalid input!")
        return


rent_a_boat()

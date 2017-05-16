# Whats for dinner

Let python determine whats for dinner.

This script fetches a JSON array with names for a dinner, and them randomly chooses them for each day of the week.

## Example

```json
[
	"Fish & Chips",
	"Soup",
	"Toast",
	"Pommes fries"
]
```

```
$ whats-for-dinner.py -s dinners.json
Dinners:
> Monday: Fish & Chips
> Tuesday: Pommes fries
> Wednesday: Toast
> Thursday: Soup
> Friday: Fish & Chips
> Saturday: Soup
> Sunday: Toast
```

## License

MIT


*Made by Edvin Hultberg in 2017*


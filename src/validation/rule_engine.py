def validate_specs(specs_list):
    validated_results = []

    for specs in specs_list:
        issues = []

        if not specs.get("horsepower"):
            issues.append("Missing horsepower")

        if not specs.get("engine_type"):
            issues.append("Missing engine type")

        specs["issues"] = issues
        specs["is_valid"] = len(issues) == 0
        specs["confidence_score"] = max(0, 100 - len(issues) * 20)

        validated_results.append(specs)

    return validated_results

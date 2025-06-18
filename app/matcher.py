from difflib import SequenceMatcher

def jaccard_similarity(set1, set2):
    intersection = len(set(set1) & set(set2))
    union = len(set(set1) | set(set2))
    return intersection / union if union != 0 else 0

def string_similarity(str1, str2):
    return SequenceMatcher(None, str1.lower(), str2.lower()).ratio()

def find_best_match(input_data, student_pool, config):
    best_match = None
    best_score = 0

    for candidate in student_pool:
        if candidate["student_id"] == input_data["student_id"]:
            continue

        # Match components
        goal_sim = string_similarity(input_data["goal"], candidate["goal"])
        study_time_match = input_data["preferred_study_time"] == candidate["preferred_study_time"]
        study_type_match = input_data["study_type"] == candidate["study_type"]
        personality_score = jaccard_similarity(input_data["personality"], candidate["personality"])
        overlap_traits = list(set(input_data["personality"]) & set(candidate["personality"]))

        # Weighted total score
        total_score = (
            goal_sim * config["boost_goal_match"]
            + (config["study_time_weight"] if study_time_match else 0)
            + (config["study_type_weight"] if study_type_match else 0)
            + personality_score * config["personality_weight"]
        )

        total_score /= (
            config["boost_goal_match"]
            + config["study_time_weight"]
            + config["study_type_weight"]
            + config["personality_weight"]
        )

        if total_score > best_score:
            matched_attrs = []
            conflicting_attrs = []

            if goal_sim >= 0.6:
                matched_attrs.append("goal")
            else:
                conflicting_attrs.append("goal")

            if study_time_match:
                matched_attrs.append("study_time")
            else:
                conflicting_attrs.append("study_time")

            if study_type_match:
                matched_attrs.append("study_type")
            else:
                conflicting_attrs.append("study_type")

            if overlap_traits:
                matched_attrs.append("personality")
            else:
                conflicting_attrs.append("personality")

            best_score = total_score
            best_match = {
                "matched_student_id": candidate["student_id"],
                "match_score": round(total_score, 2),
                "reasoning": {
                    "goal_similarity": round(goal_sim, 2),
                    "study_time_match": study_time_match,
                    "study_type_match": study_type_match,
                    "personality_overlap": overlap_traits
                },
                "explanation": {
                    "matched_attributes": matched_attrs,
                    "conflicting_attributes": conflicting_attrs
                }
            }

    if best_score >= config["minimum_match_score"]:
        return best_match
    else:
        return {
            "matched_student_id": None,
            "match_score": 0,
            "reasoning": {},
            "explanation": {
                "matched_attributes": [],
                "conflicting_attributes": []
            }
        }

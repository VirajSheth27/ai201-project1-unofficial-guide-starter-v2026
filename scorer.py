def judge(question: str, expects: str, answer: str, results) -> bool:
       if not expects or not answer:
           return False
       return expects.strip().lower() in answer.lower()
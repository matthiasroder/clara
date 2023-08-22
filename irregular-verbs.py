import random

# List of irregular verbs
# Each entry is a tuple containing the base form, past simple, and past participle
irregular_verbs = [
("begin", "began", "begun"),
("break", "broke", "broken"),
("bring", "brought", "brought"),
("build", "built", "built"),
("buy", "bought", "bought"),
("catch", "caught", "caught"),
("choose", "chose", "chosen"),
("come", "came", "come"),
("cost", "cost", "cost"),
("cut", "cut", "cut"),
("do", "did", "done"),
("draw", "drew", "drawn"),
("drive", "drove", "driven"),
("eat", "ate", "eaten"),
("fall", "fell", "fallen"),
("feel", "felt", "felt"),
("fight", "fought", "fought"),
("find", "found", "found"),
("fly", "flew", "flown"),
("forget", "forgot", "forgotten"),
("freeze", "froze", "frozen"),
("get", "got", "gotten/got"),
("give", "gave", "given"),
("go", "went", "gone"),
("grow", "grew", "grown"),
("have", "had", "had"),
("hear", "heard", "heard"),
("hide", "hid", "hidden"),
("hit", "hit", "hit"),
("hold", "held", "held"),
("hurt", "hurt", "hurt"),
("keep", "kept", "kept"),
("know", "knew", "known"),
("lead", "led", "led"),
("leave", "left", "left"),
("lend", "lent", "lent"),
("let", "let", "let"),
("lie", "lay", "lain"),
("lose", "lost", "lost"),
("make", "made", "made"),
("mean", "meant", "meant"),
("meet", "met", "met"),
("pay", "paid", "paid"),
("put", "put", "put"),
("read", "read", "read"),
("ride", "rode", "ridden"),
("ring", "rang", "rung"),
("rise", "rose", "risen"),
("run", "ran", "run"),
("say", "said", "said"),
("see", "saw", "seen"),
("sell", "sold", "sold"),
("send", "sent", "sent"),
("set", "set", "set"),
("shake", "shook", "shaken"),
("shine", "shone", "shone"),
("shoot", "shot", "shot"),
("show", "showed", "shown/showed"),
("shut", "shut", "shut"),
("sing", "sang", "sung"),
("sink", "sank", "sunk"),
("sit", "sat", "sat"),
("sleep", "slept", "slept"),
("slide", "slid", "slid"),
("speak", "spoke", "spoken"),
("spend", "spent", "spent"),
("stand", "stood", "stood"),
("steal", "stole", "stolen"),
("stick", "stuck", "stuck"),
("strike", "struck", "struck"),
("swear", "swore", "sworn"),
("sweep", "swept", "swept"),
("swim", "swam", "swum"),
("take", "took", "taken"),
("teach", "taught", "taught"),
("tear", "tore", "torn"),
("tell", "told", "told"),
("think", "thought", "thought"),
("throw", "threw", "thrown"),
("understand", "understood", "understood"),
("wake", "woke", "woken"),
("wear", "wore", "worn"),
("win", "won", "won"),
("write", "wrote", "written")

]

def test_irregular_verbs():
    correct_answers = 0
    num_questions = 10

    for idx, verb in enumerate(random.sample(irregular_verbs, num_questions)):
        base_form, past_simple, past_participle = verb

        print(f"Question {idx + 1}/{num_questions}: What is the past simple and past participle of '{base_form}'?")

        user_past_simple = input("Enter the past simple form: ")
        user_past_participle = input("Enter the past participle form: ")

        if user_past_simple.lower() == past_simple and user_past_participle.lower() == past_participle:
            print("Correct!\n")
            correct_answers += 1
        else:
            print(f"Incorrect. The correct answers are: Past Simple - {past_simple}, Past Participle - {past_participle}\n")

    print(f"Test finished. You answered {correct_answers} out of {num_questions} correctly.")

if __name__ == "__main__":
    test_irregular_verbs()


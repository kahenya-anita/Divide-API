from app import app, db, Divide

def seed_data():
    with app.app_context():
        db.create_all()

        sample_data = [
            {"a": 10, "b": 5, "result": 10 // 5},
            {"a": 20, "b": 4, "result": 20 // 4},
            {"a": 15, "b": 3, "result": 15 // 3},
            {"a": 9, "b": 3, "result": 9 // 3},
            {"a": 100, "b": 25, "result": 100 // 25},
        ]

        for data in sample_data:
            division_result = Divide(a=data["a"], b=data["b"], result=data["result"])
            db.session.add(division_result)

        db.session.commit()
        print("Database seeded!")

if __name__ == '__main__':
    seed_data()
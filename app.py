# code for sotring images using mongodb

from flask import Flask, jsonify, request, current_app, render_template, session, send_file, send_from_directory
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from flask_cors import CORS
import requests

from pymongo import errors
from datetime import datetime
import secrets
import os

app = Flask(__name__, static_folder='static')
bcrypt = Bcrypt(app)
CORS(app)


app.config['MONGO_URI'] = 'mongodb://localhost:27017/agist-db'
app.config['SECRET_KEY'] = b'606c367f499e04db'

mongo = PyMongo(app)


@app.route('/home', methods=['GET', 'POST'])
def home():

    cursor = mongo.db.fixtures.find()
    fixture_list = []
    for _ in cursor:
        for i in cursor:
            fixture_list.append({'_id': str(i['_id']), 'team_a': i['team_a'], 'team_b': i['team_b'], 'time': i['time'], 'place': i['place'],  'category': i['category']})
            
            print(fixture_list)
    return render_template('index.html', fixture= fixture_list)

@app.route('/admin/home', methods=['GET', 'POST'])
def admin_home():

    cursor = mongo.db.teams.find()
    team_list = []
    for _ in cursor:
        for i in cursor:
            team_list.append({'_id': str(i['_id']), 'name': i['name'], 'logo': i['logo'], 'category': i['category']})
            
            
            print(team_list)
    return render_template('admin-home.html', teams=team_list)


@app.route('/admin/team', methods=['GET', 'POST'])
def admin_team():

    cursor = mongo.db.teams.find()
    team_list = []
    for _ in cursor:
        for i in cursor:
            team_list.append({'_id': str(i['_id']), 'name': i['name'], 'logo': i['logo'], 'category': i['category']})
            
            print(team_list)
    return render_template('admin-team.html', teams=team_list)



@app.route('/admin/result', methods=['GET', 'POST'])
def admin_result():
    cursor = mongo.db.teams.find()
    team_list = []
    for _ in cursor:
        for i in cursor:
            team_list.append({'_id': str(i['_id']), 'name': i['name'], 'logo': i['logo'], 'category': i['category']})

    return render_template('admin-result.html', teams=team_list)

@app.route('/admin/scorer', methods=['GET', 'POST'])
def admin_scorer():
    cursor = mongo.db.teams.find()
    team_list = []
    for _ in cursor:
        for i in cursor:
            team_list.append({'_id': str(i['_id']), 'name': i['name'], 'logo': i['logo'], 'category': i['category']})

    return render_template('admin-scorer.html', teams=team_list)


@app.route('/admin/award', methods=['GET', 'POST'])
def admin_award():
    cursor = mongo.db.teams.find()
    team_list = []
    for _ in cursor:
        for i in cursor:
            team_list.append({'_id': str(i['_id']), 'name': i['name'], 'logo': i['logo'], 'category': i['category']})

    return render_template('admin-award.html', teams=team_list)



@app.route('/admin/fixture', methods=['GET', 'POST'])
def admin_fixture():
    cursor = mongo.db.teams.find()
    team_list = []
    for _ in cursor:
        for i in cursor:
            team_list.append({'_id': str(i['_id']), 'name': i['name'], 'logo': i['logo'], 'category': i['category']})

    return render_template('fixture.html', teams=team_list)


@app.route('/admin/new/team', methods=['GET', 'POST'])
def new_team():

    return render_template('add-team.html')


@app.route('/about', methods=['GET', 'POST'])
def about():

    return render_template('about.html')

@app.route('/mission', methods=['GET', 'POST'])
def mission():

    return render_template('mission.html')

@app.route('/awards', methods=['GET', 'POST'])
def awards():
    cursor = mongo.db.award.find()
    award_list=[]
    for i in cursor:
        award_list.append({'_id': str(i['_id']), 'player_name': i['player_name'], 'award_name': i['award_name'], 'photo': i['photo'], 'category': i['category'], 'team': i['team'], 'age': i['age']})
  
    return render_template('awards.html', award=award_list)

@app.route('/rules', methods=['GET', 'POST'])
def rules():

    return render_template('rules.html')

@app.route('/conditions', methods=['GET', 'POST'])
def conditions():

    return render_template('conditions.html')


@app.route('/accomodation', methods=['GET', 'POST'])
def accomodation():

    return render_template('accomodation.html')

@app.route('/registration', methods=['GET', 'POST'])
def registration():

    return render_template('registration.html')

@app.route('/teams', methods=['GET', 'POST'])
def teams():
    cursor = mongo.db.teams.find()
    team_list = []
    for _ in cursor:
        for i in cursor:
            team_list.append({'_id': str(i['_id']), 'name': i['name'], 'logo': i['logo'], 'category': i['category']})

    return render_template('team.html', teams=team_list)

@app.route('/media', methods=['GET', 'POST'])
def media():

    return render_template('media.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():

    return render_template('contact.html')


@app.route('/view/<name>', methods=['GET', 'POST'])
def view(name):
    cursor = mongo.db.players.find({'team': name})
    players_list=[]
    for i in cursor:
        players_list.append({'_id': str(i['_id']), 'name': i['name'], 'category': i['category'], 'position': i['position'], 'age': i['age'], 'team': i['team'], 'photo': i['photo']})

    return render_template('view-team.html', players=players_list)


# @app.route('/view/images/<email>')
# def view_images(email):
#     user = mongo.db.users.find_one({'_id': email})
#     if len(list(user['images'])) != 0:
#         filename_list = []
#         # retrieval from mongodb        
#         cursor = mongo.db.fs.files.find({'_id': {'$in': user['images']}})
#         for _ in cursor:
#             filename_list.append(_['filename'])
#         return jsonify(filename_list)
#     else:
#         return jsonify({'msg': 'you did not uploaded any images'})



#Register
@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        encrypt_password = bcrypt.generate_password_hash(password)
        date = datetime.now()

        user_dict = {
            '_id': email,  
            'name': name,
            'password': encrypt_password,
            'date': date.strftime('%d %B %Y'),
            'images': []
        }

        try:
            mongo.db.users.insert_one(user_dict)
        except errors.DuplicateKeyError:
            return jsonify({'msg': 'user already registered'})

        return jsonify({'msg': f'User registered {name}'}), 201


# Login
@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        cursor = mongo.db.users.find_one({'_id': email})
        try:
            if 'email' in session:
                return jsonify({'msg': f'User is already logged in'})
        except KeyError:
            pass 

        if cursor != None:
            if bcrypt.check_password_hash(cursor['password'], password):
                session['email'] = email
                return jsonify({
                    'msg': f'login {cursor["name"]} successful',
                    'email': cursor['_id']
                })
            else:
                return jsonify({'msg': 'Incorrect password'})
        else:
            return jsonify({'msg': f'user {email} not found'}), 404


# Logout
@app.route('/logout', methods=['GET', 'POST'])
def logout():
    if 'email' in session:
        session.pop('email', default=None)
        return jsonify({'msg': 'successfully logged out'})
    else:
        return jsonify({'msg': 'no user logged in'})


#add team
@app.route('/admin/add/team', methods=['POST'])
def add_team():
    if request.method == 'POST':
        name = request.form.get('name')
        category = request.form.get('category')
        date = datetime.now()
        image = request.files['picture']
        _, f_ext = os.path.splitext(image.filename)
        file_extension = ['.jpg','.png','.jpeg','.svg','.JPEG', '.JPG', '.PNG', '.SVG']
        if f_ext not in file_extension:
            return jsonify({'msg': f'{image.filename} is not valid image.'
            })
        else:
            random_hex = secrets.token_hex(8)
            logo = random_hex + f_ext
            picture_path = os.path.join(current_app.root_path, 'static', logo)
            image.save(picture_path)
            mongo.save_file(logo, image)

            team_dict = {
                'name': name,
                'category': category,
                'date': date.strftime('%d %B %Y'),
                'logo': logo,
                'logo_path': picture_path,
                'players': []
            }

            try:
                mongo.db.teams.insert_one(team_dict)
            except errors.DuplicateKeyError:
                return jsonify({'msg': 'team already registered'})
            return jsonify({'msg': 'team registered'}), 201


@app.route('/admin/add/player', methods=['POST'])
def add_player():
    
    if request.method == 'POST':
        name = request.form.get('name')
        position = request.form.get('position')
        age = request.form.get('age')
        team = request.form.get('team')
        category = request.form.get('category')
        date = datetime.now()
        image = request.files['picture']
        _, f_ext = os.path.splitext(image.filename)
        file_extension = ['.jpg','.png','.jpeg','.svg','.JPEG', '.JPG', '.PNG', '.SVG']
        if f_ext not in file_extension:
            return jsonify({'msg': f'{image.filename} is not valid image.'
            })
        else:
            random_hex = secrets.token_hex(8)
            photo = random_hex + f_ext
            picture_path = os.path.join(current_app.root_path, 'static', photo)
            image.save(picture_path)
            mongo.save_file(photo, image)
            
            team_dict = {
                'name': name,
                'position': position,
                'photo': photo,
                'photo_path': picture_path,
                'team': team,
                'age': age,
                'category': category
            }
            try:
                mongo.db.players.insert_one(team_dict)
            except errors.DuplicateKeyError:
                return jsonify({'msg': 'Already exist'})

            return jsonify({'msg': f'Success'}), 201


# post image in the database
# @app.route('/upload/image', methods=['POST'])
# def upload_video():
#     if request.method == 'POST':
#         image = request.files['picture']
#         _, f_ext = os.path.splitext(image.filename)
#         file_extension = ['.jpg','.png','.jpeg','.svg','.JPEG', '.JPG', '.PNG', '.SVG']

#         if f_ext not in file_extension:
#             return jsonify({
#                 'msg': f'{image.filename} is not valid image.'
#             })
#         else:
#             _id = mongo.save_file(imagename, image)
#             mongo.db.users.update_one(
#                 filter = {
#                     '_id': session['email']
#                 },
#                 update = {
#                     '$addToSet': {
#                         'images': _id
#                     }
#                 }
#             )
#             return jsonify({'msg': f'uploaded image {image.filename}'})


# #post image 
# @app.route('/admin/upload/image', methods=['POST'])
# def upload_image():
#     if request.method == 'POST':
#         image = request.files['picture']
#         _, f_ext = os.path.splitext(image.filename)
#         file_extension = ['.jpg','.png','.jpeg','.svg','.JPEG', '.JPG', '.PNG', '.SVG']
#         if f_ext not in file_extension:
#             return jsonify({
#                 'msg': f'{image.filename} is not valid image.'
#             })
#         else:
#             random_hex = secrets.token_hex(8)
#             unique_filename =  random_hex + f_ext
#             picture_path = os.path.join(current_app.root_path, 'static', unique_filename)
#             image.save(picture_path)
#             mongo.db.users.update_one(
#                 filter = {
#                     '_id': session['email']
#                 },
#                 update = {
#                     '$addToSet': {
#                         'images': unique_filename
#                     }
#                 }
#             )
#             return jsonify({'msg': f'uploaded image {image.filename}'})



#add fixure
@app.route('/admin/add/fixture', methods=['POST'])
def add_fixture():
    if request.method == 'POST':
        team_a = request.form.get('team_a')
        team_b = request.form.get('team_b')
        place = request.form.get('place')
        date = request.form.get('date')
        time = request.form.get('time')
        category = request.form.get('category')
        # logo_a 
        # logo_b 

        # cursor_a = mongo.db.teams.find_one({'name': team_a})
        # for i in cursor_a:
        #     logo_a.append({'_id': str(i['_id']),'logo': i['logo']})

        # cursor_b = mongo.db.teams.find_one({'name': team_b})
        # for i in cursor_b:
        #     logo_a.append({'_id': str(i['_id']),'logo': i['logo']})


        fixture_dict = {
            'team_a': team_a,  
            'team_b': team_b,
            'place': place,
            'date': date,
            'time': time,
            'category': category,
            # 'logo_a': logo_a,
            # 'logo_b': logo_b,
        }

        try:
            mongo.db.fixtures.insert_one(fixture_dict)
        except errors.DuplicateKeyError:
            return jsonify({'msg': 'Already exist'})

        return jsonify({'msg': f'Success'}), 201




@app.route('/admin/add/result', methods=['POST'])
def add_result():
    if request.method == 'POST':
        team_a = request.form.get('team_a')
        team_b = request.form.get('team_b')
        score_a = request.form.get('score_a')
        score_b = request.form.get('score_b')
        date = request.form.get('date')
        time = request.form.get('time')
        category= request.form.get('category')

        result_dict = {
            'team_a': team_a,  
            'team_b': team_b,
            'date': date,
            'time': time,
            'category': category
        }

        try:
            mongo.db.results.insert_one(result_dict)
        except errors.DuplicateKeyError:
            return jsonify({'msg': 'Already exist'})

        return jsonify({'msg': f'Success'}), 201


@app.route('/admin/add/award', methods=['POST'])
def add_award():
    if request.method == 'POST':
        player_name = request.form.get('player_name')
        award_name = request.form.get('award_name')
        age = request.form.get('age')
        position = request.form.get('position')
        team = request.form.get('team')
        category= request.form.get('category')
        image = request.files['picture']
        _, f_ext = os.path.splitext(image.filename)
        file_extension = ['.jpg','.png','.jpeg','.svg','.JPEG', '.JPG', '.PNG', '.SVG']
        if f_ext not in file_extension:
            return jsonify({'msg': f'{image.filename} is not valid image.'
            })
        else:
            random_hex = secrets.token_hex(8)
            photo = random_hex + f_ext
            picture_path = os.path.join(current_app.root_path, 'static', photo)
            image.save(picture_path)
            mongo.save_file(photo, image)
            

            award_dict = {
                'player_name': player_name,  
                'award_name': award_name,
                'age': age,
                'position': position,
                'team': team,
                'photo':photo,
                'category': category
            }

            try:
                mongo.db.award.insert_one(award_dict)
            except errors.DuplicateKeyError:
                return jsonify({'msg': 'Already exist'})

            return jsonify({'msg': f'Success'}), 201


@app.route('/admin/add/scorer', methods=['POST'])
def add_scorer():
    if request.method == 'POST':
        player_name = request.form.get('player_name')
        goals = request.form.get('goals')
        age = request.form.get('age')
        position = request.form.get('position')
        team = request.form.get('team')
        category= request.form.get('category')

        scorer_dict = {
            'player_name': player_name,  
            'goals': goals,
            'age': age,
            'position': position,
            'team': team,
            'category': category
        }

        try:
            mongo.db.scorer.insert_one(scorer_dict)
        except errors.DuplicateKeyError:
            return jsonify({'msg': 'Already exist'})

        return jsonify({'msg': f'Success'}), 201


# post image in the database
# @app.route('/upload/image', methods=['POST'])
# def upload_video():
#     if request.method == 'POST':
#         image = request.files['picture']
#         _, f_ext = os.path.splitext(image.filename)
#         file_extension = ['.jpg','.png','.jpeg','.svg','.JPEG', '.JPG', '.PNG', '.SVG']

#         if f_ext not in file_extension:
#             return jsonify({
#                 'msg': f'{image.filename} is not valid image.'
#             })
#         else:
#             _id = mongo.save_file(imagename, image)
#             mongo.db.users.update_one(
#                 filter = {
#                     '_id': session['email']
#                 },
#                 update = {
#                     '$addToSet': {
#                         'images': _id
#                     }
#                 }
#             )
#             return jsonify({'msg': f'uploaded image {image.filename}'})



#view Images for particular user
@app.route('/view/images/<email>')
def view_images(email):
    user = mongo.db.users.find_one({'_id': email})
    if len(list(user['images'])) != 0:
        filename_list = []
        # retrieval from mongodb        
        cursor = mongo.db.fs.files.find({'_id': {'$in': user['images']}})
        for _ in cursor:
            filename_list.append(_['filename'])
        return jsonify(filename_list)
    else:
        return jsonify({'msg': 'you did not uploaded any images'})


#view single image
@app.route('/<filename>')
def view_image_single(filename):
    return mongo.send_file(filename)

# @app.route('/<path:filename>')  
# def send_file(filename):  
#     return send_from_directory(app.static_folder, filename)


# delete single file
@app.route('/delete/image/<imagename>', methods=['DELETE'])
def delete_image(imagename):
    user = mongo.db.users.find_one({'images': imagename})
    if session['email'] == user['_id']:    
        if user:
            os.remove(os.path.join(current_app.root_path, 'static', imagename))
            mongo.db.users.update_one(
                filter = {
                    '_id': session['email']
                },
                update = {
                    '$pull': {
                        'images': imagename
                    }
                }
            )
            return jsonify({
                'msg': f'image {imagename} is deleted'
            })
        else:
            return jsonify({
                'msg': f'image {imagename} not found'
            }), 404
    else:
        return jsonify({
            'msg': 'not authorized.'
        }), 401


      
@app.route('/admin/view/teams')
def view_teams():
    cursor = mongo.db.teams.find()
    team_list = []
    for _ in cursor:
        for i in cursor:
            team_list.append({'_id': str(i['_id']), 'name': i['name'], 'category': i['category'], 'logo': i['logo_path']})
    if len(list(team_list)) == 0:
        return jsonify({'msg': 'no image found'})
    else:
        return jsonify(team_list)


@app.route('/admin/view/fixture', methods=['GET'])
def view_fixture():
    cursor = mongo.db.fixtures.find()
    fixture_list = []
    for _ in cursor:
        for i in cursor:
            fixture_list.append({'_id': str(i['_id']), 'team_a': i['team_a'], 'category': i['category']})
    if len(list(fixture_list)) == 0:
        return jsonify({'msg': 'no image found'})
    else:
        return jsonify({'fixtures': fixture_list})


@app.route('/admin/view/team', methods=['GET'])
def view_team():
    cursor = mongo.db.teams.find()
    team_list = []
    for _ in cursor:
        for i in cursor:
            team_list.append({'_id': str(i['_id']), 'name': i['name'], 'logo': i['logo_path']})
    if len(list(team_list)) == 0:
        return jsonify({'msg': 'no image found'})
    else:
        return jsonify({'teams': team_list})
      

if __name__ == "__main__":
    app.run(debug=True)
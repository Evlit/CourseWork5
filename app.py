from flask import Flask, render_template, request, redirect, url_for

from base import Arena
from classes import unit_classes
from unit import PlayerUnit, EnemyUnit
from utils import get_result, get_heroes

app = Flask(__name__)

arena = Arena() 


@app.route("/")
def menu_page():
    return render_template('index.html')


@app.route("/fight/")
def start_fight():
    heroes = get_heroes(False, False)
    arena.start_game(player=heroes['player'], enemy=heroes['enemy'])
    return render_template("fight.html", heroes=heroes)


@app.route("/fight/hit")
def hit():
    heroes = get_heroes(False, False)
    if arena.game_is_running:
        result = arena.player_hit()
    else:
        result = arena.battle_result

    return render_template("fight.html", heroes=heroes, result=result)


@app.route("/fight/use-skill")
def use_skill():
    heroes = get_heroes(False, False)
    if arena.game_is_running:
        result = arena.player_use_skill()
    else:
        result = arena.battle_result

    return render_template("fight.html", heroes=heroes, result=result)


@app.route("/fight/pass-turn")
def pass_turn():
    heroes = get_heroes(False, False)
    if arena.game_is_running:
        result = arena.next_turn()
    else:
        result = arena.battle_result

    return render_template("fight.html", heroes=heroes, result=result)


@app.route("/fight/end-fight")
def end_fight():
    heroes = get_heroes(False, False)
    return render_template("index.html", heroes=heroes)


@app.route("/choose-hero/", methods=['get', 'post'])
def choose_hero():
    if request.method == 'GET':
        result = get_result('Выбор героя')
        return render_template("hero_choosing.html", result=result)

    if request.method == 'POST':
        name = request.form.get('name')
        unit_class = request.form.get('unit_class')
        weapon_name = request.form.get('weapon')
        armor_name = request.form.get('armor')
        player = PlayerUnit(name, unit_classes[unit_class], weapon_name, armor_name)
        get_heroes('player', player)
        return redirect(url_for("choose_enemy"))


@app.route("/choose-enemy/", methods=['post', 'get'])
def choose_enemy():
    if request.method == 'GET':
        result = get_result('Выбор героя')
        return render_template("hero_choosing.html", result=result)

    if request.method == 'POST':
        name = request.form.get('name')
        unit_class = request.form.get('unit_class')
        weapon_name = request.form.get('weapon')
        armor_name = request.form.get('armor')
        enemy = EnemyUnit(name, unit_classes[unit_class], weapon_name, armor_name)
        get_heroes('enemy', enemy)
        return redirect(url_for("start_fight"))


if __name__ == "__main__":
    app.run()

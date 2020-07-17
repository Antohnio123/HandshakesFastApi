#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;
int Round = 1;
bool Pdrowned;   // Игрок утонул
bool Mdrowned;  // Монстр утонул
int Direction; // направление стрельбы игрока
int I=1; // мишень Монстра
bool mozila = false; // стрелял в противоположную монстру сторону - пока не понятно, как проверить (способ простой, но не срабтаывает)
bool dostal = false;
bool otbil = false;
bool AllahAkbar = false; // самоподрыв на гранате

class weapon {
public:
	int t, range, damage, push;
	enum type { пистолет = 1, огнемёт, гранаты };
	weapon () {
		//int t;
		cout << "Подготовка к бою." << endl<< "Выберите оружие: 1 - пистолет,  2 - огнемёт, 3 - гранаты" << endl;
		cin >>t;
		srand(time(NULL));
		switch (t) {
		case пистолет: 
			this->range = 20;
			this->damage = 10 + rand() % 20;
			this->push = 1;
			cout  << "Вы выбрали пистолет, он стреляет далеко, урон равен " << damage << ", отталкивает противника на 1 клетку." << endl;
			break;
		case огнемёт:
			this->range = 3;
			this->damage = 1 + rand() % 10;
			this->push = 0;
			cout  << "Вы выбрали огнемёт, он жгёт напалмом " << range << " клетки в сторону от Вас, урон равен " << damage << ", противника НЕ отталкивает, но поджигает" << endl;
			break;
		case гранаты:
			this->range = 4;
			this->damage = 30 + rand() % 20;
			this->push = 2;
			cout << "Вы выбрали гранаты, они бросаются на " << range << " клетки, урон наносится 3 клеткам: мишени и каждой соседней клетке. Урон равен " << damage << ", каждого попавшего в зону поражения отталкивает на "<< push << " клетки" << endl;
			break;
		default:
			cout << "Выберите оружие, введя число от 1 до 3, где 1 - пистолет,  2 - огнемёт, 3 - гранаты. Других вариантов нет. " << endl;
		}

	}
	~weapon() { cout << "Вы выбросили оружие, оно уничтожено в пропасти"<< endl; };
};
class Monster;
class Player;

class Player {
friend class Monster;
friend class weapon;
public:
	bool on_fire = false;
	int place = 1;
	int h = 100;
	void attack (Monster &m, weapon &w); //приходится лишь обозначать функцию тут, чтобы описать ниже, под полным описанием класса Monster
		
	~Player() { cout << "Вы убиты молнией" << endl; };
};


class Monster {
friend class weapon; 
friend class Player; 
public:
	int armour;
	enum armour { пистолет = 1, огнемёт, гранаты }; 
	int place = 10;
	bool on_fire = false;
	int damage = 50; 
	int h = 100;
	void attack(Player &p);
	void intension(Player &p);
	~Monster() { cout << "Монстр убит молнией" << endl; };
};

void Monster::intension(Player &p) {
	I = p.place;
	/*srand(time(NULL));*/
	place = 1 + rand() % 10;
	while (place == p.place)
	{
		/*srand(time(NULL));*/
		place = 1 + rand() % 10;
	};
	cout << "Вы стоите на клетке " << p.place << endl;
	cout << "Монстр передвигается на клетку " << place << endl;
	srand(time(NULL));
	damage = 10 + rand() % 60;
	cout << "Монстр собирается бросить камень на клетку " << I << ", нанеся урон " << damage << " единиц этой клетке и клеткам с " << I - 2 << " по " << I + 2 << endl;
	armour = 1 + rand() % 4;
	cout << "Монстр покрылся бронёй: ";
		switch (armour) {
		case пистолет: cout << "- противопульная -" << endl << endl; break;
		case огнемёт: cout << "- огнеупорная - " << endl << endl; break;
		case гранаты: cout << "- противоосколочная - " << endl << endl; break;
		default: cout << "- нет брони - " << endl << endl;
		};
}
void Monster::attack (Player &p) {
	cout << "Монстр бросат камень! Камень летит на клетку " << I << ", а игрок перешёл = " << p.place << endl;
	if (on_fire == true) { h -= 10; cout << "Монстр горит! Огнём монстру нанесно 10 единиц урона. Здоровье Монстра равно " << h << endl; };
	if (h <= 0) { cout << "Монстр мёртв. Вы сожгли его и победили! Поздравляем. " << endl;
	system("pause");
	exit(0);
	};
	if (I - 2 <= p.place and p.place <= I + 2) {
			p.h -= damage;
			cout << "Монстр бросает камень на клетку " << I << " и цепляет Вас осколками камня! Наносит Вам "<< damage << " урона.  У Вас остаётся "<< p.h << " единиц здоровья" << endl;
	}
	else cout << "Монстр бросает камень на клетку " << I << " и промахивается. Вы увернулись!" << endl;
	if (I - 2 <= place and place <= I + 2) {
		h -= damage;
		cout << "Монстр задевает камнем и себя!  Здоровье Монстра уменьшено и равно "<< h << endl;
		if (h <= 0) { 
			cout << "Монстр убил сам себя...  Естественный отбор выбрал Вас как более умную особь. Вы победили, поздравляем!" << endl << endl;
			system("pause");
			exit(0);
		};
	}
	
}

void Player::attack (Monster &m, weapon &w) {
	// сначала проверяем эффект горения и смерти от него
	cout << "Ваш ход." << endl;
	if (on_fire == true) {
		h -= 10; 
		cout << "Огнём Вам нанесно 10 единиц урона. Здоровье Ваше равно " << h << endl; 
	};
	if (h <= 0) {
		cout << "GAME OVER. \n Вы сгорели... До угольков. А Вы думали, что огнемётом можно чистить себе обувь? \n Монстр покушал шашлык, хотя не особо и старался. Попробуйте ещё раз!" << endl << endl;
		system("pause");
		exit(0);
	};
	// теперь позволяем игроку передвинуться
	do {
		cout << "Введите номер клетки, на которую хотите перепрыгнуть" << endl;
		cin >> place; 
		if (place == m.place) { 
			cout << "Это Вам не Марио, на голову Монстру прыгать нельзя!" << endl;
		};
	}		while (place == m.place);
	if (place > 10 or place < 1) { 
		Pdrowned = true; cout << "Надо же, игрок утопился сам. Монстр подавился от смеха, хахаха." << endl << endl;
		system("pause");
		exit(0);
	};
	// предлагаем игроку выстрелить в монстра, выбрав направление стрельбы
	if (w.t != 3) {
		cout << "Укажите, в какую сторону хотите стрелять, введите номер какой-нибудь ячейки, в сторону которой направите своё оружие" << endl;
	} else cout << "Укажите, на какую ячейку бросите гранату" << endl;
	cin >> Direction;
	// сталкиваем игрока с тяжёлыми последствими стрельбы себе в ногу
	if (Direction == place) {
		h -= w.damage;
		if (w.t != 3) {
			cout << "Вы выстрелили себе в ногу, Ваше здоровье понизилось и равно " << h << endl;
		}
		else { 
			cout << "Вы бросили гранату под себя! Ваше здоровье понизилось и равно " << h << ", а наша вера в Вас почти иссякла..." << endl;
		};
		if (w.t == 2) {
			on_fire = true; cout << "Вы подожгли себя огнемётом!   Вы прям жжёте, Вы зажигалка! " << endl;
		};
	};
	// проверяем, не выстрелил ли в противоположную монстру сторону (1)
		//int fnc1 () { 
	//	place - Direction> 0 ? 1: -1;
	//};
	//int fnc2() {
	//	place - m.place> 0? 1: -1;
	//};
	//bool Pricel = false;
	//if (fnc1 == fnc2) { 
	//	Pricel = true; cout << "Вы выстрелили в правильном направлении" << endl; 
	//} else cout << "Вы выстрелили в противоположном монстру направлении" << endl;


	// проверяем, хватило ли range оружия, чтобы достать монстра (2) для гранаты прописать +1 к рэнджу
	if (w.t != 3) {
		if (w.range >= abs(place - m.place)) {
			dostal = true;
		}
		else dostal = false;
	}
	else if (w.range + 1 >= abs(place - m.place)) { // если граната, то хватает ли дальности броска +1 рэндж от урона, чтобы достать Монстра? (2-2)
		dostal = true;
			if (abs(m.place - Direction) > 1) {  // проверяем, что наоборот, если слишком близко Монстр, а бросалась граната далеко, не было ли перелёта с учётом, что кроет она 3 клетки (2-2)
				dostal = false;
					cout << "Граната перелетела.  Вы ж не ядро на Олимпиаде швыряете... тут точность нужна." << endl;
			};
	}
	else {
		dostal = false;
			cout << "Далеко. Гранату не добросить. " << endl;
	};
	
	
			
				
	// проверяем, не совпала ли броня монстра с типом нашего оружия (3) 
	if (m.armour == w.t) {
		otbil = true;
	}	else otbil = false;
	// если попали по монстру и броня не сработала, наносим урон и отталкиваем монстра ТОЛЧОК НЕ В ТУ СТОРОНУ!!!!!!!!!!!!!!!!!!!!!, проверяем, не загорелся ли, не утоп ли и не сдох ли
	if (mozila == true) {
		cout << "Вы выстрелили в противоположном монстру направлении. Здоровье монстра = " << m.h << endl;
	}
	else if (dostal == false) {
		cout << "Оружие не причинило урон противнику (не достало). Здоровье монстра = " << m.h << endl;
	}
	else if (otbil == true) {
		cout << "Броня монстра сдержала атаку. Урон нанесён не был. Здоровье монстра = "<< m.h << endl;
		m.place < place ? m.place -= w.push : m.place += w.push;
		w.push > 0 ? cout << "Монстр сдвинут на " << w.push << " клеток и находится на клетке " << m.place << endl : cout << "Монстр остался на своём месте" << endl;
		m.place < 1 or m.place > 10 ? Mdrowned = true : Mdrowned = false;
	}
	else { // просчитываем попадание!
		m.h -= w.damage;
		cout << "Вы попали по монстру. Здоровье монстра = " << m.h << endl;
		m.place < place ? m.place -= w.push : m.place += w.push;
		w.push > 0 ? cout << "Монстр сдвинут на " << w.push << " клеток и находится на клетке " << m.place << endl : cout << "Монстр остался на своём месте" << endl;
		m.place < 1 or m.place > 10 ? Mdrowned = true : Mdrowned = false;
		w.t == 2 ? m.on_fire = true: m.on_fire = false;
	};

	// проверяем, не утоп ли и не сдох ли игрок от гранаты
	if (w.t == 3) {
		if (abs(place - Direction) <= 1) {
		AllahAkbar = true;
		h -= w.damage;
		cout << "Вы зацепили себя гранатой. Вам наносится урон и Вас отбрасывает в сторону!" << endl;
		if (Direction < place) {
			place += 2;
		}
		else place -= 2;
		place < 1 or place > 10 ? Pdrowned = true : Pdrowned = false;
		}
	};

	if (Pdrowned == true) { cout << "Надо же, игрок утопился сам. Монстр подавился от смеха, хахаха." << endl << endl;
	system("pause");
	exit(0);
	}
	else if (Mdrowned == true) { 
		if (h > 0) {
			cout << "Вы сбросили Монстра в пропасть! Он погиб. Поздравляем, Вы победили!" << endl << endl;
			system("pause");
			exit(0);
		}	else cout << "Вы сбросили Монстра в пропасть! Но и сами погибли.  Ничья..." << endl << endl;
	}
	else if (m.h <= 0) {
		if (h > 0) {
			cout << "Монстр убит! Поздравляем, Вы победили!" << endl << endl;
			system("pause");
			exit(0);
		} else cout << "Вы убили Монстра! И себя.  Зато теперь на мосту воцарилась полная тишина и покой.  Game Over" << endl << endl;
	} 	else if (h <= 0) { cout << "Вы погибли! Гранаты детям не игрушка.  Монстр слизывает Ваши остатки с моста. Game Over" << endl << endl;
			system("pause");
			exit(0);
		};
	//закончить!
};




int main(int argc, const char * argv[]) {
	setlocale(LC_ALL, "rus");
	cout << "Вы сражаетесь с Монстром на мосту над пропастью с лавой" << endl
	<< "Мост соединяет два маленьких островка."<<endl
	<< "Есть 10 клеток в ряд, на которых Вы или монстр можете стоять." << endl
	<< "Первая клетка, левая - Ваш остров, 10-я клетка, правая - остров Монстра." << endl
	<< "Левее 1-й клетки и правее 10-й клетки - пропасть." <<endl
	<< "Вы с Монстром перепрыгиваете на любую свободную клетку и стреляете влево или вправо" << endl
	<< "Монстр может менять плотность соей шкуры, получая разного вида броню на один ход" << endl << endl;
	
	weapon PW;
	Player Man;
	Monster Naag;
	
	do {
		cout << endl << endl << "Раунд № " << Round << endl;
		Round++;
		cout << "Ваше здоровье = " << Man.h << ", здоровье монстра = " << Naag.h << endl;
		Naag.intension (Man);
		//Man.Move;
		Man.attack(Naag,PW); 
		Naag.attack(Man);
		if (Pdrowned == true) {
			cout << "Вы сброшены в пропасть. Монстр победил." << endl;
			system("pause");
			exit(0);
		}		else if (Mdrowned == true) {
					cout << "Монстр упал в пропасть! И погиб. Поздравляем, Вы победили!" << endl;
					system("pause");
					exit(0);
				}		else if (Man.h <= 0) { 
							cout << "Вы погибли! Монстр оказался сильнее, но попробуйте ещё раз, Вы его переиграете!" << endl;
							system("pause");
							exit(0);
						}		else if (Naag.h <= 0) {
								cout << "Монстр убит! Поздравляем, Вы победили!" << endl;
								system("pause");
								exit(0);
								};
		system("pause");
		// тут надо описать ход раунда
	}	while (Round <= 10); 
		
	cout << endl<< "Вы не убили Монстра за 10 раундов? Ну Вы даёте... пошёл дождь и вывел Ваше оружие из строя. Монср посмеялся и проглотил Вас целиком" << endl;


	system ("pause");
	return 0;
}
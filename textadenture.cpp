#include <iostream>
#include <string.h>
#include <string>

int end = 0;

std::string g_eventval = "";
std::string dicision = "";

int g_movementval[4] = {0, 1, 2, 3};

enum ITEMIDS {
  ladder = 1,
};

std::string ITEMIDSS[]{"ERROR ITEM", "laddder", "test"};

struct {
  int g_playerinventory[10]{0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

} g_playerstats;
struct {
  int ROOM14 = 0;
  int ROOM7 = 0;
} FLAGROOMS;

int returnDirectionVal(std::string p_2) {
  if (p_2 == "forward") {
    return g_movementval[0];
  }
  if (p_2 == "backwards") {
    return g_movementval[1];
  }
  if (p_2 == "right") {
    return g_movementval[2];
  }
  if (p_2 == "left") {
    return g_movementval[3];
  }
  return -1;
}

static const void updateDirectionVals(int t_f, int t_b, int t_r, int t_l) {
  g_movementval[0] = t_f;
  g_movementval[1] = t_b;
  g_movementval[2] = t_r;
  g_movementval[3] = t_l;
}

static const void listControls(int t_controlToList) {
  switch (t_controlToList) {
  case 0:
    std::cout << "\nYou cannot walk here\n";
    break;
  case 1:
    std::cout << "\nYou can walk: forward, backwards, left and right\n";
    break;
  case 2:
    std::cout << "\nYou can pickup the item, or simply leave it.\n";
    break;
  case 3:
    std::cout << "Are you sure?\nyes/no: ";
    break;
  case 4:
    std::cout << "Invalid command, please type again\n";
    break;
  case 5:
    std::cout << "Pickup item?\nyes/no: ";
    break;
  default:
    std::cout << "Dev error! Incorrect t_controlToList variable: "
              << t_controlToList << "\n";
    break;
  }
}

static const int choice(int t_controltolist) {
  int choice = 0;
  std::string choicestr;
  listControls(t_controltolist);
  std::cin >> choicestr;
  choice = choicestr == "yes" ? 1 : 0;
  return choice;
}

static const void listPlayerInventory() {
  for (int i = 0; i < 10; i++) {
    if (g_playerstats.g_playerinventory[i] != 0) {
      std::cout << ITEMIDSS[i + 1];
    }
  }
}

static const void playerEventPickUp(int item, int &FLAG) {
  if (choice(3) == 1) {
    for (int i = 0; i < 10; i++) {
      if (g_playerstats.g_playerinventory[i] == 0) {
        g_playerstats.g_playerinventory[i] = item;
        FLAG += 1;
        break;
      }
    }
  }
}

static const void textLookUpTable(int t_textEvent, int flag = 0) {
  switch (t_textEvent) {
  case 0:
    std::cout << "\nYou return from where you came from. \n";
    break;
  case 10:
    std::cout
        << "You are a young knight on a quest to slay the mysterious monster "
           "whom is feared by everyone in the kingdom of Kowardly. Staring at "
           "the giant cave entrance, it fills you with fear.\n";
    break;
  case 11:
    std::cout << "As a proud citizen of KOWARDLY you ponder for a moment if "
                 "you should go back to your parents empty handed.\n";
    break;
  case 12:
    std::cout << "You stick hurry back to your parents crying. The end.\n";
    break;
  case 13:
    std::cout
        << "You find youself in a cave. The walls are howling as the cold wind "
           "streams into the cave, almost like a current of water pulling you "
           "down. No way back young knight. Proceed further into the cave.";
    break;
  case 14:
    if (FLAGROOMS.ROOM14 == 1) {
      textLookUpTable(0);
    } else {
      std::cout << "You go deeper into the cave.\n";
    }
    std::cout << "To the right you find a small "
                 "door. To the left lies an old crooked ladder. Ahead of you "
                 "is a dimly lit well, only visible due to the faint light "
                 "comming from the entrance of the cave.";
    break;
  case 15:
    std::cout << "You go to the small door";
    break;
  case 16:
    std::cout << "You go to the old crooked ladder.";
    break;
  case 17:
    std::cout
        << "Well, that is a well. You hear rats from the bottomless darkness.";
    break;
  default:
    std::cout << "You messed! Program your game better next time!";
    break;
  }
}

static const void eventLookUpTable(int t_event) {
  switch (t_event) {
  case 0:
    textLookUpTable(13);
    updateDirectionVals(4, 2, 2, 2);
    break;
  case 1:
    textLookUpTable(11);
    dicision = "";
    while (dicision != "yes" & dicision != "no") {
      listControls(3);
      std::cin >> dicision;
    }
    if (dicision == "yes") {
      textLookUpTable(12);
      end = 1;
    } else if (dicision == "no") {
      break;
    }
    break;

  case 2:
    listControls(0);
    break;
  case 4: // Cave
    textLookUpTable(14);
    FLAGROOMS.ROOM14 = 1; // "You go back" sentence
    updateDirectionVals(5, 0, 6, 7);
    break;
  case 5: // Well
    textLookUpTable(17);
    updateDirectionVals(2, 4, 2, 2);
    break;
  case 6: // Small Door
    textLookUpTable(15);
    updateDirectionVals(2, 4, 2, 2);
    break;
  case 7: // Ladder
    if (FLAGROOMS.ROOM7 == 0) {
      textLookUpTable(16);
      listControls(2);
      playerEventPickUp(ladder, FLAGROOMS.ROOM7);
      listPlayerInventory();
    }

    updateDirectionVals(2, 4, 2, 2);
    break;
  }

  std::cout << "\n";
}

int main() {
  textLookUpTable(10);
  listControls(1);

  while (end != 1 && std::cin >> g_eventval) {

    while (returnDirectionVal(g_eventval) == -1) {
      listControls(4);
      std::cin >> g_eventval;
    }
    eventLookUpTable(returnDirectionVal(g_eventval));
  }
}
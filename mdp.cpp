#include<bits/stdc++.h>
#define lsc(x) scanf("%lld",&x)
#define sc(x) scanf("%d",&x)
#define lpr(x) printf("%lld ",x)
#define pr(x) printf("%d ",x)
#define n_l printf("\n")
#define VI vector<int>
#define VII vector<long long int>
#define m_p make_pair
#define pb push_back
#define fi first
#define se second
#define mset(x,y) memset(x,y,sizeof(x))
using namespace std;
const int N=(int)1e3+5;
const int mod = 1000000007;
typedef long long ll;
//vector<int>::iterator itr=lower_bound(v.begin(),v.end(),x);
double walls[N][N], state[N][N], mat[N][N], a[N][N], b[N][N];
double score;
int n,m;

bool isvalid(int x, int y){
    if (x < 0 || y < 0 || x >= n || y >= m)
        return false;
    if (walls[x][y])
        return false;
    return true;
}

double update(int x,int y){
    int idx[] = { -1, 0, 0, 1, 0, -1, 1, 0};
    double util[4] = {0.0};
    for (int i=0;i<4;i++){
        if( isvalid(x+idx[2*i], y+idx[2*i+1] )){
            util[i] = b[x+idx[2*i]][y+idx[2*i+1]] + mat[x+idx[2*i]][y+idx[2*i+1]];
        }
        else{
            util[i] = b[x][y] + mat[x][y];
        }
    }
    double north = 0.8 * util[0] + 0.1 * util[1] + 0.1 * util[2];
    double east = 0.8 * util[1] + 0.1 * util[0] + 0.1 * util[3];
    double west = 0.8 * util[2] + 0.1 * util[0] + 0.1 * util[3];
    double south = 0.8 * util[3] + 0.1 * util[1] + 0.1 * util[2];
    double maxm = max(max(north, east), max(west, south));
    return maxm + score;
}

void solve(){
    int count =0;
    int itr =0;
    while(count != n*m){
        count = 0;
        for (int i=0;i<n;i++) for (int j=0;j<m;j++) b[i][j] = a[i][j];
        for (int i=0;i<n;i++){
            for (int j=0;j<n;j++){
                if (state[i][j] || walls[i][j]) {
                    count++;
                    continue;
                }
                a[i][j] = update(i,j);
                if (    
                        ((b[i][j]*0.99 < a[i][j] ) && (a[i][j] < 1.01*b[i][j])) || 
                        ((b[i][j]*0.99 > a[i][j] ) && (a[i][j] > 1.01*b[i][j]))
                   ) count++;
            }
        }
        for (int i=0;i<n;i++){
            for (int j=0;j<m;j++)
                cout<<a[i][j]<<" ";
            n_l;
        }
        pr(++itr);pr(count);n_l;
    }
}



int main(){
    sc(n);sc(m);
    for (int i=0;i<n;i++){
        for (int j=0;j<m;j++){
            cin >> a[i][j];
            b[i][j] = a[i][j];
            mat[i][j] = a[i][j];
        }
    }
    int nwall, nend;
    sc(nend);sc(nwall);
    for (int i=1;i<=nend;i++) {
        int x,y;
        sc(x);sc(y);
        state[x][y]=1;
        mat[x][y] = 0;
    }
    for (int i=1;i<=nwall;i++) {
        int x,y;
        sc(x);sc(y);
        walls[x][y]=1;
    }
    int stx, sty;
    sc(stx);sc(sty);
    cin>>score;
    for (int i=0;i<n;i++)
        for (int j=0;j<m;j++){
            a[i][j]-=mat[i][j];
            b[i][j]-=mat[i][j];
        }
    /*for (int i=0;i<n;i++){
        for (int j=0;j<m;j++)
            cout<<a[i][j]<<" ";n_l;
    }
    for (int i=0;i<n;i++){
        for (int j=0;j<m;j++)
            cout<<b[i][j]<<" ";n_l;
    }
    for (int i=0;i<n;i++){
        for (int j=0;j<m;j++)
            cout<<mat[i][j]<<" ";n_l;
    }*/
    solve();
}


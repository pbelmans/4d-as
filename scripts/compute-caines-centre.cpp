// Centre dimensions for Caines over a prime field, using exact FLINT arithmetic.
// The basis is x1^a x2^b x3^c x4^d. The six relations are a quadratic
// Groebner basis in descending generator order x4 > x3 > x2 > x1;
// this was checked with Macaulay2 for every recorded parameter sample.
// Left and right multiplication matrices are built recursively from the
// previous degree, avoiding repeated reductions of long noncommutative words.
// The centre is the common kernel of the four commutator matrices.
//
// Compile (Homebrew paths; adjust for another installation):
// c++ -O3 -std=c++17 -I/opt/homebrew/include scripts/compute-caines-centre.cpp -L/opt/homebrew/lib -lflint -o /tmp/compute-caines-centre
// Arguments: prime maximum_degree a b c d [matrix_dump_path].
// The optional dump records the eight multiplication matrices in the last degree.
// Samples, timings, and cross-checks are in scripts/caines-centre-results.json.
#include <flint/nmod_mat.h>
#include <flint/ulong_extras.h>
#include <array>
#include <chrono>
#include <iostream>
#include <fstream>
#include <map>
#include <memory>
#include <vector>
using E = std::array<int,4>;
using Clock = std::chrono::steady_clock;
struct Matrix {
    nmod_mat_t m;
    Matrix(long r,long c,ulong p) { nmod_mat_init(m,r,c,p); }
    ~Matrix() { nmod_mat_clear(m); }
    ulong& at(long r,long c) { return nmod_mat_entry(m,r,c); }
};
using Ptr = std::unique_ptr<Matrix>;
using Maps = std::array<Ptr,4>;
struct Basis {
    std::vector<E> words;
    std::map<E,long> indices;
    Basis(int n) {
        for(int a=0;a<=n;a++) for(int b=0;b<=n-a;b++) for(int c=0;c<=n-a-b;c++) {
            E e{a,b,c,n-a-b-c}; indices[e]=words.size(); words.push_back(e);
        }
    }
    long size() const { return words.size(); }
    long index(E e) const { return indices.at(e); }
};
struct Term { int a,b; ulong coefficient; };
ulong power(ulong a,ulong n,ulong p) {
    ulong r=1; for(;n;n>>=1,a=a*a%p) if(n&1) r=r*a%p; return r;
}
int main(int argc,char** argv) {
    if(argc!=7 && argc!=8) return 2;
    ulong p=std::stoul(argv[1]); int maxDegree=std::stoi(argv[2]);
    if(maxDegree<1 || p<3 || p>1000000000 || !n_is_prime(p)) return 2;
    auto residue=[&](const char* s) { long v=std::stol(s); return ulong((v%long(p)+p)%p); };
    ulong a=residue(argv[3]),b=residue(argv[4]),c=residue(argv[5]),d=residue(argv[6]);
    if(!c) return 2;
    ulong bc=b*power(c,p-2,p)%p, bdc=bc*d%p, bbdcc=bc*bc%p*d%p;
    std::vector<Term> rewrite[4][4];
    rewrite[1][0]={{0,1,p-1}};
    rewrite[2][0]={{0,2,1},{0,3,(p-bdc)%p},{1,3,d}};
    rewrite[2][1]={{1,2,1},{1,3,(p-bdc)%p},{0,3,bbdcc}};
    rewrite[3][0]={{2,2,c},{0,3,p-1}};
    rewrite[3][1]={{2,2,b},{1,3,p-1}};
    rewrite[3][2]={{2,3,1},{0,1,a}};
    Maps previousLeft,previousRight;
    Basis one(1);
    for(int i=0;i<4;i++) {
        previousLeft[i]=std::make_unique<Matrix>(4,1,p);
        previousRight[i]=std::make_unique<Matrix>(4,1,p);
        E e{};e[i]=1; long row=one.index(e);
        previousLeft[i]->at(row,0)=previousRight[i]->at(row,0)=1;
    }
    auto start=Clock::now();
    for(int n=1;n<=maxDegree;n++) {
        auto step=Clock::now();
        Basis before(n-1),current(n),after(n+1);
        std::vector<long> columns[4],rests[4];
        for(long col=0;col<current.size();col++) {
            E e=current.words[col];int j=0;while(!e[j])j++;
            e[j]--;columns[j].push_back(col);rests[j].push_back(before.index(e));
        }
        Maps left,right;
        auto product=[&](int generator,Matrix& previous,int j) {
            Matrix selected(current.size(),rests[j].size(),p);
            for(long r=0;r<current.size();r++) for(long k=0;k<long(rests[j].size());k++)
                selected.at(r,k)=previous.at(r,rests[j][k]);
            auto result=std::make_unique<Matrix>(after.size(),rests[j].size(),p);
            if(generator<=1) {
                for(long r=0;r<current.size();r++) {
                    E e=current.words[r];bool negative=generator==1 && (e[0]%2);
                    e[generator]++;long target=after.index(e);
                    for(long k=0;k<long(rests[j].size());k++) {
                        ulong v=selected.at(r,k);
                        result->at(target,k)=negative && v ? p-v : v;
                    }
                }
            } else nmod_mat_mul(result->m,left[generator]->m,selected.m);
            return result;
        };
        for(int i=0;i<4;i++) {
            left[i]=std::make_unique<Matrix>(after.size(),current.size(),p);
            for(int j=0;j<4;j++) {
                if(i<=j) {
                    for(long col:columns[j]) { E e=current.words[col];e[i]++;left[i]->at(after.index(e),col)=1; }
                } else for(auto term:rewrite[i][j]) {
                    auto values=product(term.a,*previousLeft[term.b],j);
                    for(long r=0;r<after.size();r++) for(long k=0;k<long(columns[j].size());k++) {
                        ulong &v=left[i]->at(r,columns[j][k]);
                        v=(v+term.coefficient*values->at(r,k))%p;
                    }
                }
            }
        }
        for(int i=0;i<4;i++) {
            right[i]=std::make_unique<Matrix>(after.size(),current.size(),p);
            for(int j=0;j<4;j++) {
                auto values=product(j,*previousRight[i],j);
                for(long r=0;r<after.size();r++) for(long k=0;k<long(columns[j].size());k++)
                    right[i]->at(r,columns[j][k])=values->at(r,k);
            }
        }
        Matrix commutators(4*after.size(),current.size(),p);
        for(int i=0;i<4;i++) for(long r=0;r<after.size();r++) for(long col=0;col<current.size();col++)
            commutators.at(i*after.size()+r,col)=(left[i]->at(r,col)+p-right[i]->at(r,col))%p;
        auto mapsDone=Clock::now();
        long dimension=current.size()-nmod_mat_rank(commutators.m);
        auto end=Clock::now();
        auto seconds=[](auto x,auto y){return std::chrono::duration<double>(y-x).count();};
        std::cout<<"DEGREE "<<n<<" DIM "<<dimension<<" MAP_SECONDS "<<seconds(step,mapsDone)
                 <<" RANK_SECONDS "<<seconds(mapsDone,end)<<" TOTAL_SECONDS "<<seconds(start,end)<<std::endl;
        if(argc==8 && n==maxDegree) {
            std::ofstream file(argv[7]);
            for(int side=0;side<2;side++) for(int i=0;i<4;i++) {
                Matrix& matrix=side ? *right[i] : *left[i];
                for(long r=0;r<after.size();r++) for(long col=0;col<current.size();col++)
                    file<<matrix.at(r,col)<<" ";
                file<<"\n";
            }
        }
        previousLeft=std::move(left);previousRight=std::move(right);
    }
}
